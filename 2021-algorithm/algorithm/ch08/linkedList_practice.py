class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def getDataIndex(self, data):
        curn = self.head
        idx = 0
        while curn:
            if curn.data == data:
                return idx
            curn = curn.next
            idx += 1
        return -1

    def insertNodeAtIndex(self, idx, node):
        curn = self.head
        prevn = None
        cur_i = 0

        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
            else:
                self.head = node
        else:
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = curn
                prevn.next = node
            else:
                return -1


    def insertNodeAtData(self, data, node):
        idx = self.getDataIndex(data)
        if 0 <= idx:
            self.insertNodeAtIndex(idx, node)
        else:
            return -1

    def deleteAtIndex(self, idx):
        cur_i = 0
        curn = self.head
        prevn = None
        nextn = self.head.next
        if idx == 0:
            self.head = nextn
        else:
            while cur_i < idx:
                if curn.next:
                    prevn = curn
                    curn = nextn
                    nextn = nextn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                prevn.next = nextn
            else:
                return -1

    def clear(self):
        self.head = None

    def print(self):
        curn = self.head
        string = ""
        while curn:
            string += str(curn.data)
            if curn.next:
                string += "->"
            curn = curn.next
        print(string)


if __name__ == '__main__':
    s1 = SingleLinkedList()
    s1.append(Node(1))
    s1.append(Node(2))
    s1.append(Node(3))
    s1.append(Node(5))
    s1.insertNodeAtIndex(3, Node(4))
    s1.print()
