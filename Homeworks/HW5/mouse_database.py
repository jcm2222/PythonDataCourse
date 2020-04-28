import datajoint as dj

schema = dj.schema('mousedata')


@schema
class MouseID(dj.Manual):
    definition = """
    # mouse id table
    mouse_id : int  # id for mouse subject
    ---
    age : float # age of mouse in weeks
    sex : enum('F', 'M')  # sex of mouse
    comments = null : varchar(4000)
    """

@schema
class Drug(dj.Manual):
    definition = """
    # drug administered table
    drug : varchar(10) # full name of drug administered
    ---
    dose : float # dose of the drug given, in mg/kg
    route : enum('i.p.','s.c.','i.v.') # method of admistering
    comments = null : varchar(1000)
    """


@schema
class Behavior(dj.Manual):
    definition = """
    # behavior table
    behavior_name : varchar(31) # short name for stimulus
    ---
    behavior_type : enum('anxiety','fear','depressive-like','motor','baseline') # beh type
    duration : float # in minutes
    """


@schema
class CalciumData(dj.Manual):
    definition = """
    # full mouse data
    -> MouseID
    recording_id : int
    ---
    -> Drug
    experimenter : varchar(100)
    comments = null : varchar(4000)
    ---
    -> Behavior
    behavior_room : varchar(20)
    """
