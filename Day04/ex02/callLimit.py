def callLimit(limit: int):
    cnt = 0

    def callLimiter(function):
        def limitFunction(*args, **kwargs):
            try:
                nonlocal cnt
                if cnt < limit:
                    cnt += 1
                    return function(*args, **kwargs)
                else:
                    raise AssertionError(f"The function {function.__name__}\
                                        has been called too many times")
            except AssertionError as e:
                print(AssertionError.__name__ + ":" + str(e))
            except Exception as e:
                print(f"An error occurred: {e}")

        return limitFunction

    return callLimiter