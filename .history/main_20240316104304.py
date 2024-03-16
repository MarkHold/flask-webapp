from website import create_app

app = create_app()

# The if __name__ == '__main__': block is used to check if the script is being run directly,
if __name__ == '__main__':
   # debug=True makes the server restart after everytime you save
    app.run(debug=True)
