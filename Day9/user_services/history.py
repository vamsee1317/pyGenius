history = {}

# Add history
def add_history(userName, ticketData):
    if userName not in history:
        history[userName] = []
        history[userName].append(ticketData)

# View History:

def view_history(userName):
    return history.get(userName, [])