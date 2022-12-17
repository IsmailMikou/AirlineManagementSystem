# AUTHOR: ISMAIL MIKOU
# TITLE: AirlineManagementSystem - FINAL PROJECT
# COURSE: CMPSC-363- Intro to Database Systems.
# Professor: J. Xu.


from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
