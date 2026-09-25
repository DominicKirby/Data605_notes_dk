import event
import person

id1 = person.Person(1, "Alice")
id2 = person.Person(2, "Bob")
id3 = person.Person(3, "Charlie")
id4 = person.Person(4, "David")
id5 = person.Person(5, "Eve")
id6 = person.Person(6, "Frank")
id7 = person.Person(7, "George")
id8 = person.Person(8, "Harriet")
id9 = person.Person(9, "Ian")
id10 = person.Person(10, "John")
id11 = person.Person(11, "Kevin")
id12 = person.Person(12, "Lois")
id13 = person.Person(13, "Michael")
id14 = person.Person(14, "Ollie")
id15 = person.Person(15, "Philip")
id16 = person.Person(16, "Quinn")
id17 = person.Person(17, "Robbie")
id18 = person.Person(18, "Sarah")
id19 = person.Person(19, "Thomas")
id20 = person.Person(20, "William")
id21 = person.Person(21, "Wendy")
id22 = person.Person(22, "Wilson")
id23 = person.Person(23, "Yara")
id24 = person.Person(24, "Zack")
id25 = person.Person(25, "Amber")
id26 = person.Person(26, "Brian")
id27 = person.Person(27, "Chloe")
id28 = person.Person(28, "Daniel")
id29 = person.Person(29, "Emma")
id30 = person.Person(30, "Felix")
id31 = person.Person(31, "Grace")
id32 = person.Person(32, "Hannah")
id33 = person.Person(33, "Isaac")
id34 = person.Person(34, "Jessica")
id35 = person.Person(35, "Kyle")
id36 = person.Person(36, "Luna")
id37 = person.Person(37, "Mason")
id38 = person.Person(38, "Nora")
id39 = person.Person(39, "Owen")
id40 = person.Person(40, "Penelope")
id41 = person.Person(41, "Ryan")
id42 = person.Person(42, "Sophia")
id43 = person.Person(43, "Tyler")
id44 = person.Person(44, "Victoria")
id45 = person.Person(45, "Wyatt")
id46 = person.Person(46, "Xander")
id47 = person.Person(47, "Zoe")
id48 = person.Person(48, "Blake")
id49 = person.Person(49, "Daisy")
id50 = person.Person(50, "Ethan")

python_workshop = event.Event("Python Workshop", 20)
five_a_side = event.Event("5 a side football", 20)
basketball = event.Event("Basketball", 10)
yoga = event.Event("Yoga", 10)
charity_fundraiser = event.Event("Charity Fundraiser", 50)

python_workshop.add_attendee([id1, id2, id3, id4, id5, id6, id7, id8, id20, id35])

five_a_side.add_attendee([id9, id10, id11, id12, id13, id14, id15, id16, id30, id41, id12])

basketball.add_attendee([id17, id18, id19, id20, id21, id22, id23, id24])

yoga.add_attendee([id25, id26, id27, id28, id30, id31, id32, id33, id49])

charity_fundraiser.add_attendee([id35, id15, id40, id33, id39, id42])

events = [python_workshop, five_a_side, basketball, yoga, charity_fundraiser]

registered_participants = [id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11, id12, id13, id14, id15, id16, id17, id18, id19, id20, id21, id22, id23, id24, id25, id26, id27, id28, id29, id30, id31, id32, id33, id34, id35, id36, id37, id38, id39, id40, id41, id42, id43, id44, id45, id46, id47, id48, id49, id50]

registered_id = []

for participant in registered_participants:
    registered_id.append(participant.id)

print(id1.id)