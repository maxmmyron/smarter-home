current_state = HomeState()

schedules = [[timeA, schedule_stateA], [timeB, schedule_stateB], ...]


def loop:
    input_state = check_input()

    schedule_state = check_schedule()

    # target state is inputstate if provided, otherwise schedule state
    target_state = input_state or schedule_state

    if (target_state == None)  # break

    changes = update_state(current_state, target_state)

    update_db(changes)

    update_vis(current_state)

    loop()
