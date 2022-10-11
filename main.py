"""
PyAvatar - sort and display avatars by website. 
Copyright (C) 2020-2022 @willtheorangeguy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Import Statements
from tkinter import *
import webbrowser

# Account Avatar Function
row_count = 2
column_count = 1

# PyAvatar Window
def avatars():
    # Build Window
    window = Tk()
    window.title("Online Account Avatars and Banners")

    # Window Title
    title = Label(
        window, text="Online Account Avatars and Banners", fg="blue", font="Consolas 20"
    )
    title.grid(row=1, column=1, columnspan=5)

    # Placeholder Image Constant
    PLACEHOLDER = PhotoImage(file="PyAvatar/images/placeholder.gif")

    # Account Link Function
    def link(url):
        webbrowser.open_new(url)

    def accounts(image, name, hyperlink):
        # Build each account frame
        account = Frame(window)
        img_account = image  # needs to be a GIF
        title_account = Label(account, image=img_account)
        text_account = Label(account, text=name)
        hyperlink_account = Label(account, text=hyperlink, fg="blue", cursor="hand2")

        # Layout elements in frame
        title_account.pack(side=TOP)
        text_account.pack(side=BOTTOM)
        hyperlink_account.pack(side=BOTTOM)
        hyperlink_account.bind("<Button-1>", lambda e: link(hyperlink))

        # Layout elements in window
        global row_count
        global column_count
        if column_count <= 5:
            account.grid(row=row_count, column=column_count, padx=5, pady=5)
            column_count += 1
        else:
            row_count += 1
            column_count = 1
            account.grid(row=row_count, column=column_count, padx=5, pady=5)

    # Account Profiles
    accounts(PLACEHOLDER, "GitHub", "https://github.com")
    accounts(PLACEHOLDER, "GitLab", "https://gitlab.com")

    # Sustain Window
    window.mainloop()


if __name__ == "__main__":
    avatars()
