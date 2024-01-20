import streamlit as st
st.set_page_config(layout='wide')

with st.expander("shape area calculator"):
    st.code(
        """
        import java.util.Scanner;

public class shapecalc {
    public static void main(String[] args) {
        System.out.println("shape area calculator");
        Scanner s=new Scanner(System.in);
        System.out.println("enter the shape");
        String  o=s.next();
        switch(o){
            case "circle":
                float a;
                int r;
                System.out.println("enter r");
                r=s.nextInt();
                a = (float) (3.14 * r * r);
                System.out.println(a);
                break;
            case "triangle":
                int l=100,b=20;
                float t;
                t = (float) (0.5 * l * b);
                System.out.println(t);
                break;
            case "tropezium":
                System.out.println("enter x");
                int x=s.nextInt();
                System.out.println("enter y");
                int y=s.nextInt();
                System.out.println("enter h");
                int h=s.nextInt();
                float z=((x+y)/2)*h;
                System.out.println(z);
                break;
            default:
                System.out.println("invalid ");



        }
    }
}

        """
    )