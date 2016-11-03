using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinCalculator
{
    public partial class Form1 : Form
    {
       double Value = 0;
       string opertaion = "";
       bool operation_pressed = false;
        public Form1()
        {
            InitializeComponent();
        }

        private void ButtonClick(object sender, EventArgs e)
        {
          
            if ((ResultTextBox.Text == "0")|| (operation_pressed))
            {
                ResultTextBox.Clear();
                
            }
            operation_pressed = false;
            Button b = (Button)sender;
            ResultTextBox.Text = ResultTextBox.Text + b.Text;
            
        }

        private void OperatorClick(object sender, EventArgs e)
        {
            Button b = (Button)sender;
            Value = double.Parse(ResultTextBox.Text);
            opertaion = b.Text;
            operation_pressed = true;

        }

        private void ButtonClick1(object sender, EventArgs e)
        {
            ResultTextBox.Text = "0";
            Value = 0;
        }

        private void OperatorClick1(object sender, EventArgs e)
        {
            switch (opertaion)
            {
                case "+":
                    ResultTextBox.Text = (Value + double.Parse(ResultTextBox.Text)).ToString();
                    
                    break;
                case "-":
                    ResultTextBox.Text = (Value - double.Parse(ResultTextBox.Text)).ToString();
                    
                    break;
                case "*":
                    ResultTextBox.Text = (Value * double.Parse(ResultTextBox.Text)).ToString();
                    
                    break;
                case "/":
                    ResultTextBox.Text = (Value / double.Parse(ResultTextBox.Text)).ToString();
                    
                    break;
                default :
                    break;

                    
                    
            }

           
              
        }

        private void ButtonClick2(object sender, EventArgs e)
        {
            ResultTextBox.Text = "0";
        }
    }
}
