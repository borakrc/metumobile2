import pymysql.cursors
from Config import Config

class MetuEventsDb:
    def __init__(self):
        self.credentials = Config.metuEventsDbCredentials

    def _connect(self):
        self.connection = pymysql.connect(
            user=self.credentials.user,
            password=self.credentials.password,
            host=self.credentials.ip,
            db=self.credentials.dbName,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)

    def fetchAll(self):
        self._connect()
        with self.connection.cursor() as cursor:
            sql = """select
                    node.language,
                    node.title,
                    node.status,
                    (select event_calendar_status_tid from field_data_event_calendar_status where entity_id = node.nid) as event_status,
                    (select body_value from field_data_body where field_data_body.entity_id = node.nid and field_data_body.revision_id = node.vid and field_data_body.bundle = 'event_calendar' and field_data_body.entity_type = 'node') as description,
                    (select name from taxonomy_term_data where tid = (select field_event_category_tid from field_data_field_event_category where entity_id = node.nid)) as event_category_name,
                    (select field_event_category_tid from field_data_field_event_category where entity_id = node.nid) as event_category,
                    (select field_event_place_value from field_data_field_event_place where entity_id = node.nid) as yer,
                    (select event_calendar_date_value from field_data_event_calendar_date where entity_id = node.nid) as ilk_tarih,
                    (select event_calendar_date_value2 from field_data_event_calendar_date where entity_id = node.nid) as son_tarih,
                    (select uri from file_managed where fid=(select field_event_image_fid from field_data_field_event_image where entity_id = node.nid)) as image_uri,
                    (select field_event_image_fid from field_data_field_event_image where entity_id = node.nid) as event_image_id,
                    (select field_event_image_width from field_data_field_event_image where entity_id = node.nid) as event_image_width,
                    (select field_event_image_height from field_data_field_event_image where entity_id = node.nid) as event_image_height
                from
                    node
                where
                    node.type = 'event_calendar'
                order by
                    node.nid"""

            cursor.execute(sql)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
            result = cursor.fetchall()

            return result


    def fetchAllRaw(self):
        self._connect()
        with self.connection.cursor() as cursor:
            sql = """select
                    *
                    from
                    node
                where
                    node.type = 'event_calendar'
                order by
                    node.nid"""

            cursor.execute(sql)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
            result = cursor.fetchall()

            return result
