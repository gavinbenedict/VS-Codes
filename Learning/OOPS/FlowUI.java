import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class FlowUI {

    public FlowUI() {
        // ------------------------------------------------------------------
        // GUI Components
        // ------------------------------------------------------------------
        JFrame mainFrame = new JFrame("Flow Layout Example"); // Renamed frameObj
        JTextField inputField1 = new JTextField(10);          // Renamed t1
        JTextField inputField2 = new JTextField(10);          // Renamed t2
        JButton displayButton = new JButton("Display");       // Renamed button
        
        // This JLabel will be created and added later inside the listener
        
        // ------------------------------------------------------------------
        // Frame Setup
        // ------------------------------------------------------------------
        mainFrame.add(inputField1);
        mainFrame.add(inputField2);
        mainFrame.add(displayButton);

        mainFrame.setSize(500, 200);
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainFrame.setLayout(new FlowLayout());
        mainFrame.setVisible(true);

        // ------------------------------------------------------------------
        // Event Handling (Action Listener)
        // ------------------------------------------------------------------
        displayButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // 1. Get User Input
                String textFromField1 = inputField1.getText(); // Renamed text1
                String textFromField2 = inputField2.getText(); // Renamed text2

                // 2. Clear and Update Frame
                mainFrame.getContentPane().removeAll();
                
                // 3. Create and Configure Display Label
                JLabel outputLabel = new JLabel(); // Renamed l
                // setBounds is often ignored by FlowLayout, but kept here for original structure
                outputLabel.setBounds(20, 30, 200, 200); 
                outputLabel.setText(textFromField1 + " " + textFromField2);
                
                // 4. Add the new label and refresh the frame
                mainFrame.add(outputLabel);
                mainFrame.revalidate(); // Using revalidate is better when removing/adding components
                mainFrame.repaint();
            }
        });
    }

    public static void main(String args[]) {
        new FlowUI();
    }
}