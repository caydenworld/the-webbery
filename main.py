import csv

import streamlit as st
import streamlit.components.v1 as components


def main():
    projects = []

    # region Intro
    st.header("Hi There! I'm C98!")
    st.write(
        "This is a place where I might post what I'm working on, and keeping it as a portfolio... That's kinda it..."
    )
    st.subheader("This is the code for the website so far:")
    st.code("""st.header("Hi There! I'm C98!")
        st.write("This is a place where I might post what I'm working on, and keeping it as a portfolio... That's kinda it...")
        st.subheader("This is the code for the website so far:")""")
    st.subheader("About Me")
    st.write(
        "I am Cayden! A 16y old who enjoys programming, digital art and learning new things! I'm into blender, Open Source and all things techy! Looking forward to working more on YSWSs, meeting new people and trying new things out!"
    )
    st.write("Hackatime Stats")
    components.iframe("https://hackatime.hackclub.com/@c89", height=400, scrolling=True)

    # endregion
    # region Project Class
    class Project:
        def __init__(self, name, photo, link, time, ai_used):
            self.name = name
            self.photo = photo
            self.time = time
            self.link = link
            self.ai_used = ai_used

        def display(self, column):
            with column.container(border=True):
                st.image(self.photo)
                st.subheader(self.name)
                col1, col2 = st.columns(2)
                with col1:
                    st.link_button("View Code", self.link)
                with col2:
                    st.badge(label=self.time, icon=":material/schedule:")
                if self.ai_used:
                    st.badge(
                        label="Ai Was Used", icon=":material/smart_toy:", color="red"
                    )
                elif self.ai_used == "help":
                    st.badge(
                        label="Ai help for research, NOT CODE.",
                        icon=":material/help:",
                        color="yellow",
                    )
                else:
                    st.badge(
                        label="100% Handwritten",
                        icon=":material/code_xml:",
                        color="green",
                    )

    # endregion
    with open("projects.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            project = Project(
                name=row["name"],
                photo=row["photo"],
                link=row["link"],
                time=row["time"],
                ai_used=row["ai_used"].strip().lower() == "yes",
            )

            projects.append(project)
    st.subheader("Projects I've Made So Far")
    for start in range(0, len(projects), 3):
        columns = st.columns(3)

        batch = projects[start : start + 3]

        for column, project in zip(columns, batch):
            project.display(column)


if __name__ == "__main__":
    main()
