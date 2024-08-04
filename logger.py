class Logger:

    def __init__(self):
        self.message_timestamp = {}  # key - message; value - message timestamp
        self.last_message_timestamp = -1

    def should_print_message(self, timestamp: int, message: str) -> bool:
        if message not in self.message_timestamp:
            self.add_message(timestamp, message)
            return True
        else:
            last_timestamp = self.message_timestamp[message]
            if last_timestamp + 10 > timestamp:
                return False
            else:
                self.add_message(timestamp, message)
                return True

    def add_message(self, timestamp: int, message: str) -> None:
        if len(self.message_timestamp) == 100:
            self.message_timestamp = {}
        self.message_timestamp[message] = timestamp
        if timestamp > self.last_message_timestamp:
            self.last_message_timestamp = timestamp

    def clean(self, timestamp: int) -> bool:
        if self.last_message_timestamp + 10 <= timestamp or self.last_message_timestamp == -1:
            self.message_timestamp = {}
            return True
        else:
            return False

    def logger_size(self):
        return len(self.message_timestamp)


if __name__ == '__main__':
    logger = Logger()
    command_list = ['add', 'size', 'clean', 'quit']
    while True:
        command = input('Enter command: \n')
        if command not in command_list:
            print('Command should be on of the following', command_list, '\n')
        if command == 'add':
            try:
    	        timestamp = int(input('Enter timestamp: \n'))
            except ValueError:
                print('Invalid timestamp value, please, enter number for timestamp \n')
                continue
            message = input('Enter message: \n')
            if logger.should_print_message(timestamp, message):
                print('Message "{}" added successfully to logger \n'.format(message))
            else:
                print('Failed to add message "{}" to logger \n'.format(message))
        elif command == 'size':
            print('Current logger size: {} \n'.format(logger.logger_size()))
        elif command == 'clean':
            try:
    	        timestamp = int(input('Enter timestamp: \n'))
            except ValueError:
                print('Invalid timestamp value, please, enter number for timestamp \n')
                continue
            if logger.clean(timestamp):
                print('Successfully cleaned logger \n')
            else:
                print('Failed to clean logger. Logger is busy \n')
        elif command == 'quit':
            print('Bye-bye!')
            break
