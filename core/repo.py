from scheduler import build_schedule


def add_topic(conn, title, notes, learned_on, span_months):
    revision_schedule = build_schedule(learned_on, span_months)

    with conn:
        topic_cursor = conn.execute('''
                            INSERT INTO topics (title, notes, learned_date, span)
                            VALUES (?,?,?,?)''', 
                            (title, notes, learned_on.isoformat(), span_months)
                            )
        topic_id = topic_cursor.lastrowid

        for interval, due in revision_schedule:
            conn.execute('''
                INSERT INTO revisions (topic_id, interval, org_due_date, cur_due_date)               
                VALUES (?,?,?,?)''', 
                (topic_id, interval, due.isoformat(), due.isoformat())
                )

    return topic_id
