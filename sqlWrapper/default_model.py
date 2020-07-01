from sqlalchemy.exc import IntegrityError

from representable import Representable
import json

def get_default_model_class(db):
    class Model(Representable):
        """Baseclass for custom user models."""

        @classmethod
        def exists(cls, **attrs):
            """Returns whether an object with these attributes exists."""
            equery = cls.query().filter_by(**attrs).exists()
            return bool(db.session.query(equery).scalar())

        @classmethod
        def create(cls, **attrs):
            """Create and persist a new record for the model, and returns it."""
            return cls(**attrs).save()

        @classmethod
        def create_or_first(cls, **attrs):
            """Tries to create a new record, and if it fails
            because already exists, return the first it founds."""
            try:
                return cls.create(**attrs)
            except IntegrityError:
                db.session.rollback()
                return cls.first(**attrs)

        def update(self):
            db.session.commit()
            return self
        @classmethod
        def sqlCodeToJson(cls, sqlCode):
            result = db.session.execute(sqlCode)

            # If no rows were returned (e.g., an UPDATE or DELETE), return an empty list
            if result.returns_rows == False:
                response = []

            # Convert the response to a plain list of dicts
            else:
                response = [dict(row.items()) for row in result]

            # Output the query result as JSON
            rdata = json.dumps(response, ensure_ascii=False)
            return json.loads(rdata)

        @classmethod
        def first(cls, **attrs):
            """Returns the first object found with these attributes."""
            return cls.query().filter_by(**attrs).first()

        @classmethod
        def first_or_error(cls, **attrs):
            """Returns the first object found with these attributes
            or raises a `ValuError` if it doesn't find one."""
            obj = cls.first(**attrs)
            if obj is None:
                raise ValueError
            return obj

        @classmethod
        def query(cls):
            return db.session.query(cls)

        def save(self):
            """Adds the updated object to the current session and commits."""
            db.session.add(self)
            db.session.commit()
            return self

        def delete(self):
            """Removes the object from the current session and commits."""
            db.session.delete(self)
            db.session.commit()

    return Model
