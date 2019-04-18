from flask import Flask, render_template
import main_breadthfirst

app = Flask(__name__)



@app.route('/', methods=['GET'])
def main():


    main_breadthfirst.shuffle()
    initialState = main_breadthfirst.initial_state
    print initialState
    main_breadthfirst.breadth_first(initialState)
    moves = main_breadthfirst.backtrace()
    print moves

    return render_template('index.html', initial=initialState, moves=moves)

app.run(debug=True)
