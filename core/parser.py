def parse_input(user_input):
        if not user_input:
            return []
        return [w.strip() for w in user_input.split(',')]
    