import pathlib
from datetime import datetime
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Frame, Paragraph, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet

W_DAYS = 20
TK_VALUE = 20

__OUT_DIR_NAME = "fluturasi"
__OUT_DIR = pathlib.Path(__file__).parent.joinpath(__OUT_DIR_NAME)

FILES_DIR = pathlib.Path(__file__).parent.joinpath("files")

# Layout coordinates
PAGE_PADDING = 2 * cm

F1_H = 2 * cm
F1_W = 17 * cm
F1_Y = A4[1] - F1_H - PAGE_PADDING

F2_H = 6 * cm
F2_W = 17 * cm
F2_Y = F1_Y - F2_H

F3_Y = F2_Y - F1_H


def draw_logo_frame(canvas):
    frame = Frame(PAGE_PADDING, A4[1] - PAGE_PADDING, F2_W, F1_H)
    frame.add(
        Image(FILES_DIR.joinpath("sears.jpeg"), width=3.3 * cm, height=1 * cm),
        canvas
    )


def draw_personal_info(canvas, full_name, company_name):
    f1 = Frame(PAGE_PADDING, F1_Y, F1_W, F1_H, showBoundary=1)

    stylesheet = getSampleStyleSheet()
    p_style = stylesheet["Heading4"]
    p_style.alignment = 1  # centrat
    p1 = Paragraph(f"SC {company_name} SRL", p_style)

    p2_style = stylesheet["Normal"]
    p2 = Paragraph(f"Angajat: {full_name.title()}", p2_style)

    p3 = Paragraph(f"Generat la: {datetime.now().strftime('%d.%m.%Y')}", p2_style)

    f1.add(p1, canvas)
    f1.add(p2, canvas)
    f1.add(p3, canvas)

    f1.drawBoundary(canvas)


def draw_taxes(canvas, gross_salary):
    f2 = Frame(PAGE_PADDING, F2_Y, F2_W, F2_H, showBoundary=1)
    t_style = TableStyle(
        [
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ]
    )
    matrix = [
        ["Salariu brut:", gross_salary],
        ["CASS 25%", gross_salary * 0.25],
        ["CAS 10%", gross_salary * 0.1],
        ["Impozit", gross_salary * 0.1],
        ["Taxe 45%:", gross_salary * 0.45],
        ["Salariu net:", gross_salary * 0.65],
    ]
    t1 = Table(matrix, style=t_style, colWidths=F2_W / 2)
    f2.add(t1, canvas)

    f2.drawBoundary(canvas)


def draw_summary(canvas, gross_salary, days_off):
    stylesheet = getSampleStyleSheet()

    f3 = Frame(PAGE_PADDING, F3_Y, F1_W / 2, F1_H, showBoundary=1)
    f4 = Frame(PAGE_PADDING + F1_W / 2, F3_Y, F1_W / 2, F1_H, showBoundary=1)

    p_drepturi = Paragraph(
        f"TOTAL DREPTURI: {gross_salary * 0.65} RON", stylesheet["Heading5"]
    )
    f3.add(p_drepturi, canvas)

    # add flowables in frame 4
    p_bonuri = Paragraph(
        f"Valoare bonuri de masa: {(W_DAYS - days_off) * TK_VALUE} lei",
        stylesheet["Heading5"],
    )

    f4.add(p_bonuri, canvas)

    f3.drawBoundary(canvas)
    f4.drawBoundary(canvas)


def generate(full_name, gross_salary, days_off, company_name):
    """Generate pay slip PDF."""
    __OUT_DIR.mkdir(exist_ok=True)
    canv = Canvas(str(__OUT_DIR.joinpath(f"{full_name}.pdf")), pagesize=A4)

    draw_logo_frame(canv)
    draw_personal_info(canv, full_name, company_name)
    draw_taxes(canv, gross_salary)
    draw_summary(canv, gross_salary, days_off)

    canv.showPage()
    canv.save()