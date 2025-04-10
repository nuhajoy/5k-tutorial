class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        newstr = ""
        i = 0 
        while i < len(command):
            if command[i:i+2] == "()":
                newstr += "o"
                i += 2 
            elif command[i:i+4] == "(al)":
                newstr += "al"
                i += 4 
            else:
                newstr += command[i]
                i += 1  
        return newstr
    
        # return command.replace("()", "o").replace("(al)", "al")
