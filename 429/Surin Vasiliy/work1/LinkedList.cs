namespace work1
{
    internal class Node
    {
        public string value;
        public Node? next;

        public Node(string _val)
        {
            value = _val;
        }

        public Node(string _val, Node _next)
        {
            value = _val;
            next = _next;
        }
    }

    internal class LinkedList
    {
        private Node head;
        public int length = 0;

        public void Add(string val)
        {
            if (head == null)
            {
                head = new Node(val);
                head.next = null;
            }
            else
            {
                Node curr = head;
                while (curr.next != null) 
                {
                    curr = curr.next;
                }
                curr.next = new Node(val);
            }
            length += 1;
        }

        public void Insert(string val, int ind)
        {
            Node curr = head;
            if (ind == 0)
            {
                head = new Node(val, curr);
            }
            else
            {
                if (ind >= length)
                    ind = length;
                if (curr != null)
                {
                    for (int i = 0; i < ind - 1; i++)
                    {
                        curr = curr.next;
                    }
                    Node temp = curr.next;
                    curr.next = new Node(val, temp);
                }
                else
                {
                    Add(val);
                }
            }
            length += 1;
        }

        public void Remove(string val)
        {
            Node curr = head;
            if (curr.value == val)
            {
                head = curr.next;
                length -= 1;
                return;
            }

            for (int i = 0; i < length; i++)
            {
                if (curr.next.value == val)
                {
                    curr.next = curr.next.next;
                    length -= 1;
                    return;
                } 
                else
                {
                    curr = curr.next;
                }
            }
        }

        public Node Get(int ind)
        {
            Node curr = head;
            for (int i = 0; i < ind; i++)
            {
                curr = curr.next;
            }

            return curr;
        }

    }
}