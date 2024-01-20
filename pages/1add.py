import streamlit as st
st.title("SWITCH STATEMENT")

st.code(
    """
    import java.util.Scanner;

public class calc {
    public static void main(String[] args) {
        System.out.println("simple calculator");
        float n1,n2;
        char o;
        Scanner s=new Scanner(System.in);
        System.out.println("enter n1:");
        n1=s.nextFloat();
        System.out.println("enter n2:");
        n2=s.nextFloat();
        System.out.println("enter the operation");
        o=s.next().charAt(0);
        switch(o){
            case '+':
                System.out.println(n1+n2);
                break;
            case '_':
                System.out.println(n1-n2);
                break;
            case '*':
                System.out.println(n1*n2);
                break;
            case '/':
                System.out.println(n1/n2);
                break;
            default:
                System.out.println("invalid input");
        }

    }
}
    """
)
