# Observer pattern is used when there is one-to-many relationship between objects such as
# if one object is modified, its depenedent objects are to be notified automatically.
# (also know as Pub-Sub pattern)


class Publisher {
    constructor(subs = []) {
        this.subs = subs
    }
    subscribe(name) {
        this.subs.push(name)
    }
    unsubscribe(name) {
        this.subs = this.subs.filter(sub => sub !== name)
    }
    notify(msg) {
        for (let sub of this.subs) {
            sub.getNotified(msg)
        }
    }
}

class Subscriber {
    constructor(name) {
        this.name = name
    }
    getNotified(msg) {
        console.log(this.name, " is notified with ", msg)
    }
}

const sub1 = new Subscriber("sub1")
const sub2 = new Subscriber("sub2")
const sub3 = new Subscriber("sub3")

const pub = new Publisher()
pub.subscribe(sub1)
pub.subscribe(sub2)
pub.subscribe(sub3)

// all 3 subscribers will get notified
pub.notify(" - test msg")

pub.unsubscribe(sub2)

// only sub1 and sub3 get notified
pub.notify(" - test msg part2")
