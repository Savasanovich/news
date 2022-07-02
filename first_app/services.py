from django.db import connection


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_news(id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
                SELECT * FROM first_app_news
                
        """)
        data = dictfetchall(cursor)
    return data