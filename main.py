from pywebio.input import input, input_group, FLOAT, TEXT
from pywebio.output import put_html, put_table, put_buttons
from pywebio import start_server


def main():
    put_html("<center> <h2> Welcome to the Pywebio Example Application </h2></center>")

    user_info = input_group(
        "User Info",
        [
            input(
                "Name",
                name="name",
                type=TEXT,
                required=True,
                placeholder="Enter your name",
            ),
            input(
                "Age",
                name="age",
                type=FLOAT,
                required=True,
                placeholder="Enter your age",
            ),
            input(
                "City",
                name="city",
                type=TEXT,
                required=True,
                placeholder="Enter your city",
            ),
        ],
    )

    put_html("<center> <h2> Here is the information you entered: </h2></center>")
    put_table(
        [
            ["Field", "Value"],
            ["Name", user_info["name"]],
            ["Age", user_info["age"]],
            ["City", user_info["city"]],
        ]
    )

    put_buttons(
        ["OK"], onclick=lambda btn: put_html("<center> <h2> Thank you! </h2></center>")
    )


if __name__ == "__main__":
    start_server(main, port=8086, debug=True)
