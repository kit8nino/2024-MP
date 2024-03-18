namespace work1
{
    internal class Node
    {
        public string value;
        public int next;

        public Node(string _val, int _ind = 0)
        {
            value = _val;
            next = _ind;
        }
    }
    
    internal class LinkedList
    {
        List<Node> list;
        
        public LinkedList() { list = new List<Node>(); }

        public void Add(string val, int ind)
        {
            list.Add(new Node(val, ind));
        }

        public void insert(string val, int ind)
        {
            ind -= 1;
            if (ind < 0)
            {
                ind = 0;
            }

            if (ind  == 0)
            {
                // TODO
            } 
            else
            {
                int temp = list[ind].next;
                list[ind].next = list.Count;
                list.Add(new Node(val, temp));
            }
        }

        public void Remove(string val)
        {
            for (int i = 0; i < list.Count; i++)
            {
                if (list[i].value == val)
                {
                    if (i == 0)
                    {
                        list.RemoveAt(i);
                        for (int j = 0; j <  list.Count; j++)
                        {
                            if (list[j].next != -1)
                                list[j].next -= 1;
                        }
                    } 
                    else 
                    { 
                        list[i - 1].next = list[i].next; 
                    }
                    
                }
            }
        }

        public Node get(int ind)
        {
            return list[ind];
        }
    }
}
