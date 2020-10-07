import uuid
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

BUNDLE="creds.zip"
USER='Ucomments'
PASS='Ucomments1'
KEYSPACE='comments'

class Connection:
    def __init__(self):
        self.secure_connect_bundle = BUNDLE
        self.cluster = Cluster(
            cloud={'secure_connect_bundle': self.secure_connect_bundle},
            auth_provider=PlainTextAuthProvider(USER, PASS)
        )
        self.session = self.cluster.connect(KEYSPACE)
    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()

def insert_data(currentSession):
    user_name = "testuser"
    text_prefix = 'comment from '
    my_uuid = uuid.UUID('130995ee-c697-11ea-b7a1-8c85907c08de')

    dataCount = 1000
    for i in range(dataCount):
        try:
            currentSession.execute(
                "INSERT INTO facebook (user_name, comment_time, comment_text) VALUES (%s, %s, %s)",
                [ user_name + str(i), my_uuid, text_prefix + str(i)]
            )
        except Exception as e:
            print(e)
        else:
            print(str(i) + ' record has been inserted')

if __name__ == '__main__':
    try:
        connection = Connection()
        output = connection.session.execute("SELECT * FROM system.local")
        for row in output:
            print("You are connected to cluster: ", row.cluster_name)
    except Exception as e:
        print(e)
        print("Failure")
    else: 
        print("Success")
        insert_data(connection.session)
    finally:
        connection.close()

