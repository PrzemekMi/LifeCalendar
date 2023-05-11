from PIL import Image, ImageDraw, ImageFont
from datetime import date
from dateutil.relativedelta import relativedelta
import os

dt = date.today()
wk = dt.isocalendar()[1]


def draw():
    # a3 paper size in pixels is 5031 x 3579
    a3_horizontal = 3579
    a3_vertical = 5031
    calendar = Image.new("RGB", (a3_horizontal, a3_vertical), (255, 255, 255))
    drawCalendar = ImageDraw.Draw(calendar)
    font = ImageFont.truetype("courbd.ttf", 20)

    single_box_size = 50
    number_of_weeks_in_year = 52
    year_of_born = date(1996, 8, 26)
    age_of_death_estimation = 90

    horizontal_size = single_box_size
    vertical_size = single_box_size
    horizontal_move_offset = (
        a3_horizontal - (single_box_size * number_of_weeks_in_year)
    ) / 2  # calendar start in the middle of page
    horizontal_move = horizontal_move_offset
    veritcal_move_manual_value = (
        a3_vertical - (single_box_size * age_of_death_estimation)
    ) / 2
    vertical_move = veritcal_move_manual_value
    number_of_drawn_blocks = 0

    # provide the 1st date in YYYY,MM,DD format
    date_of_born = date(1996, 8, 26)

    # provide the 1st date in YYYY,MM,DD format
    todays_date = date.today()

    weeks_since_born = int((todays_date - date_of_born).days / 7)

    for year in range(age_of_death_estimation):
        drawCalendar.text(
            xy=(horizontal_move_offset - 55, vertical_move + 12),
            text=str(year_of_born.year),
            fill="black",
            font=font,
        )  # -55 and 12 are font depandent constants, could be calculeted by getting half of block size and width

        year_of_born = year_of_born + relativedelta(years=1)
        for week in range(number_of_weeks_in_year):
            if (
                number_of_drawn_blocks - year_of_born.isocalendar()[1]
                < weeks_since_born
            ):
                # grey-out alread lived weeks
                fill_colour = (90, 90, 90)
            else:
                fill_colour = "white"

            # do not draw boxes in the beginning of the year (make them invisible by drawing them white)
            if number_of_drawn_blocks < year_of_born.isocalendar()[1]:
                outline_beginning = "white"
                fill_colour = "white"
            else:
                outline_beginning = "black"

            drawCalendar.rectangle(
                [
                    (horizontal_move, vertical_move),
                    (horizontal_size + horizontal_move, vertical_size + vertical_move),
                ],
                fill=fill_colour,
                outline=outline_beginning,
            )
            number_of_drawn_blocks += 1
            horizontal_move += single_box_size
        horizontal_move = horizontal_move_offset
        vertical_move += single_box_size

    calendar.save("life_calendar.png")


if __name__ == '__main__':
    draw()
