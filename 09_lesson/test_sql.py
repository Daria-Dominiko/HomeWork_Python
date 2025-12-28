from sqlalchemy import create_engine, text

db = create_engine("postgresql://flora:nature-fairy@5.101.50.27:5432/x_clients_db")


def test_create_subject():
    conn = db.connect()
    result = conn.execute(
        text("INSERT INTO subjects (name, description) "
             "VALUES ('Название', 'Описание') RETURNING id")
    )
    conn.commit()
    subject_id = result.scalar()

    conn.execute(text("DELETE FROM subjects WHERE id = :id"),
                 {"id": subject_id})
    conn.commit()
    conn.close()


def test_update_subject():
    conn = db.connect()
    result = conn.execute(
        text("INSERT INTO subjects (name, description) "
             "VALUES ('Название_01', 'Старое описание') RETURNING id")
    )
    conn.commit()
    subject_id = result.scalar()
    conn.close()

    conn = db.connect()
    conn.execute(
        text("UPDATE subjects SET name = 'Название_02', "
             "description = 'Новое описание' WHERE id = :id"),
        {"id": subject_id}
    )
    conn.commit()
    conn.close()

    conn = db.connect()
    conn.execute(text("DELETE FROM subjects WHERE id = :id"),
                 {"id": subject_id})
    conn.commit()
    conn.close()


def test_delete_subject():
    conn = db.connect()
    result = conn.execute(
        text("INSERT INTO subjects (name, description) "
             "VALUES ('Название дел', 'Удали меня полностью') RETURNING id")
    )
    conn.commit()
    subject_id = result.scalar()
    conn.close()

    conn = db.connect()
    conn.execute(
        text("DELETE FROM subjects WHERE id = :id"),
        {"id": subject_id}
    )
    conn.commit()
    conn.close()
