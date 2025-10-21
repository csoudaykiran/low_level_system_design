class YoutubeChannel:
    def __init__(self):
        self.__subscribers = []  # 🔒 Private list of subscribers

    def subscribe(self, subscriber):
        """Add a new subscriber"""
        self.__subscribers.append(subscriber)
        print(f"✅ {subscriber.name} subscribed to the channel")

    def unsubscribe(self, subscriber):
        """Remove a subscriber"""
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)
            print(f"❌ {subscriber.name} unsubscribed from the channel")
        else:
            print(f"⚠️ {subscriber.name} is not subscribed")

    def upload_video(self, video):
        """Upload a new video and notify all subscribers"""
        print(f"\n📺 Channel uploaded: {video}")
        self.__notify_all(video)

    def __notify_all(self, video):
        """Private method to notify all subscribers"""
        for subscriber in self.__subscribers:
            subscriber.notify(video)


class Subscriber:
    def __init__(self, name):
        self.name = name

    def notify(self, video):
        print(f"📢 {self.name} got notified about: {video}")


# --- Testing ---
channel = YoutubeChannel()

# 🎬 Create subscribers
alice = Subscriber("Alice")
bob = Subscriber("Bob")
charlie = Subscriber("Charlie")

# ✅ Subscribing
channel.subscribe(alice)
channel.subscribe(bob)
channel.subscribe(charlie)

# 🎥 Upload first video
channel.upload_video("video 1")

# ❌ Unsubscribe one
channel.unsubscribe(bob)

# 🎥 Upload another video
channel.upload_video("Video 2")
