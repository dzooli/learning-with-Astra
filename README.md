# My Learning with Astra #

## Explain your use case ##

Just a basic idea to collect facebook comments and analyze them later within a more advanced application.

## Create your own tables on Astra ##

Show us your own tables - for the data model of your choice.

```sql
use usercomments;
create table comments.facebook (
    user_name text, 
    comment_time timeuuid, 
    comment_text text, 
    primary key (user_name)
);
```

## Insert some data ##

Show off your own data inserts, into your own tables:

```python
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

```

Now show the output, for example:

```
token@cqlsh:comments> describe tables;

facebook

token@cqlsh:comments> select * from facebook ;

 user_name   | comment_text     | comment_time
-------------+------------------+--------------------------------------
 testuser765 | comment from 765 | 130995ee-c697-11ea-b7a1-8c85907c08de
   testuser8 |   comment from 8 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser352 | comment from 352 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser833 | comment from 833 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser147 | comment from 147 | 130995ee-c697-11ea-b7a1-8c85907c08de
  testuser62 |  comment from 62 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser546 | comment from 546 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser948 | comment from 948 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser143 | comment from 143 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser622 | comment from 622 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser581 | comment from 581 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser797 | comment from 797 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser428 | comment from 428 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser196 | comment from 196 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser253 | comment from 253 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser561 | comment from 561 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser169 | comment from 169 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser985 | comment from 985 | 130995ee-c697-11ea-b7a1-8c85907c08de
 testuser329 | comment from 329 | 130995ee-c697-11ea-b7a1-8c85907c08de
```

Include some screenshots!

## Experiment with CRUD and show the outputs: ##

```sql
token@cqlsh:comments> update facebook set comment_text='A brand new comment' where user_name='testuser999';
token@cqlsh:comments> select * from facebook where user_name='testuser999';

 user_name   | comment_text        | comment_time
-------------+---------------------+--------------------------------------
 testuser999 | A brand new comment | 130995ee-c697-11ea-b7a1-8c85907c08de

(1 rows)
```

```sql
token@cqlsh:comments> delete from facebook where user_name='testuser1';
token@cqlsh:comments> select * from facebook where user_name='testuser1';

 user_name | comment_text | comment_time
-----------+--------------+--------------

(0 rows)
```

Show us something similar with your own tables.

Try something different:

Check out the CQL reference and try commands that we did not use in the workshop:

https://docs.datastax.com/en/cql-oss/3.3/cql/cql_reference/cqlReferenceTOC.html

Let us know what you find:

```
token@cqlsh:comments> select user_name,comment_time,toDate(comment_time) from facebook limit 10;

 user_name   | comment_time                         | system.todate(comment_time)
-------------+--------------------------------------+-----------------------------
 testuser765 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
   testuser8 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
 testuser352 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
 testuser833 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
 testuser147 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
  testuser62 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
 testuser546 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
 testuser948 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
 testuser143 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15
 testuser622 | 130995ee-c697-11ea-b7a1-8c85907c08de |                  2020-07-15

(10 rows)
```

Or connect, read and write to your Astra database via other methods.

Simple to access my private datastore cluster. :)

```
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
```

The starry sky is the limit: Build your own app with Astra and show it off for a chance to have it included with our Sample Galleries



