from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://postgres:nata@localhost:5432/postgres"
pg = create_engine(db_connection_string)


def test_connection():
    inspector = inspect(pg)
    names = inspector.get_table_names()
    assert len(names) == 5
    assert names[1] == 'subject'


def test_select():
    connection = pg.connect()
    result = connection.execute(text('select * from subject'))
    rows = result.fetchall()

    assert rows[0] == (1, 'English')
    assert len(rows) == 15


def test_insert():
    connection = pg.connect()
    transaction = connection.begin()
    sql = text(
        'insert into subject (subject_title) values (:new_subject_title)'
        )
    rows = connection.execute(sql, {'new_subject_title': 'Visual_art'})
    transaction.commit()

    result = connection.execute(text('select * from subject'))
    rows = result.fetchall()

    assert rows[-1] == (None, 'Visual_art')
    assert len(rows) == 16

    connection.close()


def test_update():
    connection = pg.connect()
    transaction = connection.begin()
    sql = text(
        'update subject set subject_id = :subject_id \
            where subject_title = :subject_title'
        )
    rows = connection.execute(
        sql, {'subject_title': 'Visual_art', 'subject_id': 16}
        )
    transaction.commit()

    result = connection.execute(text('select * from subject'))
    rows = result.fetchall()

    assert rows[-1] == (16, 'Visual_art')
    assert len(rows) == 16

    connection.close()


def test_delete():
    connection = pg.connect()
    transaction = connection.begin()
    sql = text('delete from subject where subject_title = :subject_title')
    connection.execute(sql, {'subject_title': 'Visual_art'})
    transaction.commit()

    result = connection.execute(text('select * from subject'))
    rows = result.fetchall()
    subjects = [row[1] for row in rows]
    assert 'Visual_art' not in subjects

    connection.close()
