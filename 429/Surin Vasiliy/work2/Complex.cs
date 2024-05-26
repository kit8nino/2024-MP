namespace work2
{
    internal class Complex
    {
        public double x_, y_;
        public Complex(double x, double y)
        {
            x_ = x; 
            y_ = y;
        }

        public double abs()
        {
            return x_ * x_ + y_ * y_;
        }
    }
}
