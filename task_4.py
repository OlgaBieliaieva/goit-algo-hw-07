class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    # Додавання відповіді
    def add_reply(self, reply_comment):
        self.replies.append(reply_comment)

    # Видалення відповіді
    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    # Виведення коментарів та відповідей
    def display(self, indent=0):
        # Відображення видаленого або існуючого коментаря
        if not self.is_deleted:
            print(" " * indent + f"{self.author}: {self.text}")
        else:
            print(" " * indent + self.text)

        # Рекурсивний обхід відповідей з відступами
        for reply in self.replies:
            reply.display(indent + 4)


# Приклад використання
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()