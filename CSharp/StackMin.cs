  public class StackMin
    {
        struct MinStackElement
        {
            public int data;
            public int min;
        }

        int top = 0;
        Stack<MinStackElement> _stackMin = new Stack<MinStackElement>();

        public void Push(int data)
        {
            if (top == 0)
            {
                _stackMin.Push(new MinStackElement() { data = data, min = data });
            }
            else
            {
                var stackElement=new MinStackElement() { data = data, min = _stackMin.Peek().min };
                if (stackElement.min > data)
                    stackElement.min = data;
                _stackMin.Push(stackElement);
            }
            top++;
        }
        public int Pop()
        {
            top--;
            return _stackMin.Pop().data;
        }
        public int GetMin()
        {
            if (top == 0)
                throw new Exception("Stack is empty.");
            var min= _stackMin.Peek().min;
            return min;
        }
    }