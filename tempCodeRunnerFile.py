def connect(self):
        global Uname
        # try except block
        try:
            # Connect to the server
            client.connect((self.HOST, self.PORT))
            print("Successfully connected to server")
            MessagePage.add_message("[SERVER] Successfully connected to the server")
        except:
            messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")

        username = Uname
        if username != '':
            self.client.sendall(username.encode())
        else:
            messagebox.showerror("Invalid username", "Username cannot be empty")

        threading.Thread(target=MessagePage.listen_for_messages_from_server, args=(client, )).start()