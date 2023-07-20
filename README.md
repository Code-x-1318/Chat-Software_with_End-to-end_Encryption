# Chat-Software_with_End-to-end_Encryption
A Software with secured chatting and Facial Recognition Login/Signup


# Abstract
In an increasingly connected world, the secure transmission of data has become a critical concern. This project aimed at enhancing the security by safeguarding data during transmission and ensuring user identity verification.
The project centres around the implementation of robust encryption techniques to protect messages and files exchanged between users. End-to-end encryption ensures that data remains confidential throughout its journey, preventing unauthorized access even when passing through potentially vulnerable cloud platforms. 


# Introduction
The primary objective of this project is to develop a robust and efficient method for securing messages and files exchanged between users, even when passing through potentially vulnerable cloud platforms. To achieve this, we propose the implementation of a comprehensive set of encryption and authentication methodologies.
Securing data during transmission from a phone to a friend's device is crucial to prevent unauthorized access by third parties. To achieve this, we can consider a combination of secure data encryption and user authentication, verification, and validation methodologies.
1.	Socket Programming: Socket programming is a computer networking concept that enables communication between different devices over a network using sockets. A socket is a software-based endpoint that allows data transmission between devices. It provides a bidirectional communication channel where processes on different devices can send and receive data.
2.	End-to-End Encryption: Implementing end-to-end encryption ensures that the data remains secure throughout its journey from the sender's phone to the recipient's device, even if it passes through cloud platforms. End-to-end encryption means that the data is encrypted on the sender's device and can only be decrypted on the recipient's device, using cryptographic keys. This way, even if the data is intercepted while in transit, it remains unintelligible to any third-party trying to access it.
3.	Symmetric Key Encryption: To reduce the computational overhead and improve transmission time, we can use symmetric key encryption for the actual data encryption. In this method, the sender and recipient share a secret key, which is used both for encryption and decryption. Symmetric key encryption is generally faster than asymmetric encryption, which requires separate public and private keys.
4.	Two-Factor Authentication (2FA): To verify the identity of the user, a two-factor authentication (2FA) mechanism can be implemented. A facial biometric authentication is required. 
By combining these secure encryption and authentication methodologies, a system is built that significantly reduces the risk of data being accessed by unauthorized parties and provides a safer way for users to share messages and files with their friends. Remember that no system can be completely immune to attacks, but by following these practices, this system significantly increases the security of data transmission and user identity verification.


# Methodology
1.)	Socket Programming
Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server. 
a.)Stages for Server
The server listens for incoming client connections and allows multiple clients to join and exchange messages in a chat room.
1.	listen_for_messages(client, username): This function is run in a separate thread for each connected client. It continuously listens for incoming messages from a specific client, appends the username to the message, and then sends the modified message to all active clients using the send_messages_to_all function.
2.	send_message_to_client(client, message): This function sends a message to a specific client. It encodes the message and sends it over the client's socket connection.
3.	send_messages_to_all(message): This function broadcasts a message to all currently connected clients. It loops through the active_clients list and calls send_message_to_client for each client to send the message.
4.	client_handler(client): This function is executed in a separate thread for each connected client. It waits for the client to send its username to the server. Once the username is received, it adds the client to the active_clients list and sends a prompt message to all clients informing them that a new user has joined. Afterward, it starts a new thread to call the listen_for_messages function for that client.
5.	main(): The main function sets up the server socket, binds it to the specified host and port, and listens for incoming client connections. When a new client connects, it starts a new thread for that client using the client_handler function.
Overall, this script provides a basic foundation for a server that can handle multiple clients in a chat application. It enables clients to join the chat room, exchange messages with other connected clients, and interact in real-time.
b.)Stages for Client
The client can connect to a server, send and receive messages, and view the conversation in a graphical user interface (GUI).
1.	add_message(message): This function updates the GUI message box with a new message. It enables the message box, inserts the new message, and disables the message box again to prevent further edits.
2.	connect(): This function establishes a connection to the server with the provided host and port. It sends the chosen username to the server for user identification. After successful connection, it starts a new thread to listen for messages from the server.
3.	send_message(): This function sends a message entered by the user in the message textbox to the server. If the message is not empty, it sends the message over the client's socket connection.
4.	listen_for_messages_from_server(client): This function is run in a separate thread to continuously listen for incoming messages from the server. When a message is received, it extracts the username and content from the message, then calls add_message to update the GUI with the new message.
5.	GUI Setup: The script creates a graphical user interface (GUI) using the tkinter library. It consists of a top frame for entering the username and joining the chat, a middle frame to display the chat messages, and a bottom frame for entering and sending new messages.
6.	Main Function: The main function is responsible for running the GUI application by calling root.mainloop().
Overall, this script provides a simple client-side GUI for the chat application, allowing users to connect to the server, send messages, and receive messages in real-time. 


# 2.End to end encryption:
End-to-end encryption is a method of encrypting and decrypting data. It is considered very secure. The method is also known as E2EE. This is the abbreviation of the English term end-to-end encryption. End-to-end encryption uses several cryptographic methods and keys. 
The security of personal data and sensitive information is always an issue when users communicate online. In addition, data security plays a significant role for processing and storing documents or other files. Anyone who communicates with each other or processes data on the net is a potential target for attack by hackers at certain points. This danger looms in the unencrypted or poorly encoded exchange of files in cloud systems or in email communication. Without sufficient encryption, third parties gain unauthorized access to personal content. With end-to-end encryption, you protect data from theft and misuse. Often, however, the encoding is only incomplete and thus offers vulnerabilities during data transmission.
E2E encryption completely encodes data. This means that there is always a secure connection between two users on the internet or between devices and storage locations. 
The special thing about this is the owners encode their content. Cloud providers or internet providers do not gain access to data or information. The content remains securely encrypted throughout the data transmission process. The secure exchange takes place from the sender to the receiver. With the appropriate key, only the recipient can decrypt the end-to-end encrypted encoding and view and read information.
How does E2E encryption work?
End-to-end encryption works in two different ways: symmetric or asymmetric. Symmetric encryption encodes data and offers the greatest possible security through AES-256 encryption. However, this also requires the AES-256 key itself to be transmitted securely and confidentially. To ensure this, TeamDrive uses asymmetric encryption with a public key procedure. When data or messages are exchanged, each user generates a key pair.

Before we proceed to define the encrypt and decrypt methods for our AESCipher class, lets first create the __pad and __unpad methods.
a.)Pad
The __pad method receives the plain_text to be encrypted and adds a number bytes for the text to be a multiple of 128 bits. This number is stored in number_of_bytes_to_pad. Then in ascii_stringwe generate our padding character, and padding_str will contain that character times number_of_bytes_to_pad. So we only have to add padding_str at the end of our plain_text so that it is now a multiple of 128 bits.

b.)Unpad
In an opposite manner, __unpad method will receive the decrypted text, also known as plain_text and will remove all the extra added characters in the __pad method. For that we first must identify the last character and store in bytes_to_remove how many bytes we need to trim of the end of plain_text in order to unpad it.

c.)Encrypt
The encrypt method receives the plain_text to be encrypted. First we pad that plain_text in order to be able to encrypt it. After we generate a new random iv with the size of an AES block, 128bits. We now create our AES cipher with AES.new with our key, in mode CBC and with our just generated iv. We now invoke the encrypt function of our cipher, passing it our plain_text converted to bits. The encrypted output is then placed after our iv and converted back from bits to readable characters.

d.)Decrypt
In order to decrypt, we must backtrack all the steps done in the encrypt method. First we convert our encrypted_text to bits and extract the iv, which will be the first 128 bits of our encrypted_text. Much like before, we now create a new AES cipher with our key, in mode CBC and with the extracted iv. We now invoke the decrypt method of our cipher and convert it to text from bits. We remove the padding with __unpad and that’s it!


# Conclusion
In conclusion, this report has presented a comprehensive project that addresses the critical concerns of secure mobile data transmission and user identity verification. By implementing advanced encryption techniques and robust authentication methods, a platform is created that empowers users to communicate securely and share information with confidence. With data confidentiality, integrity, and user identity verification at the forefront, the project contributes to building a safer digital landscape where individuals can communicate and exchange data with peace of mind. As technology continues to advance, the continuous improvement and evolution of our secure communication system will be crucial to uphold its effectiveness in safeguarding against emerging threats and maintaining a trusted communication environment for all.
