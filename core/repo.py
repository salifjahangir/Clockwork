from scheduler import build_schedule


def add_topic(conn, title, notes, learned_on, span_months):
    revision_schedule = build_schedule(learned_on, span_months)

    with conn:
        '''
        INSERT INTO TOPICS
        '''