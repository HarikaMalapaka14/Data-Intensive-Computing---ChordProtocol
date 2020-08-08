import sys
import pandas as pd
import numpy as np

nodes = []
keys = []

if (len(sys.argv) == 2):
    print("Interactive mode")

    n = int(sys.argv[1])

    if (n < 1):
        print("N value should be greater than 1")
        print("Program terminating")
        sys.exit(0)

    max_key = np.power(2, n)
    keys_range = range(0, max_key)
    poss_keys = []
    for i in keys_range:
        poss_keys.append(i)

    n_keys = []
    for i in range(0, n):
        n_keys.append(i + 1)

    # sys.exit(0)
    try:
        while (1):

            func = input("Give the function : ")
            # print(func)
            func = func.split(" ")
            function0 = func[0]
            # print(function)
            if (function0 == 'add'):
                try:
                    num = int(func[1])
                    print("In add")
                    if (num in nodes):
                        print("ERROR: Node", num, " exists")
                        continue
                    else:
                        if (num in poss_keys):
                            nodes.append(num)
                            print("Added node ", num)
                            df = 'finger{}'.format(num)
                            locals()[df] = pd.DataFrame(columns=['No', 'keys', 'NodeId'])
                            locals()[df]['No'] = n_keys
                            locals()[df]['NodeId'] = num
                            predicissor = 'pred{}'.format(num)
                            locals()[predicissor] = 'none'
                            successor = 'suc{}'.format(num)
                            locals()[successor] = num



                        else:
                            print("ERROR: node id must be in [0,", max_key, ")")

                            continue
                except:
                    print("ERROR: invalid integer ", func[1])

            elif (function0 == 'end'):
                sys.exit(0)
            elif (function0 == 'drop'):
                try:
                    num = int(func[1])
                    if (num in nodes):
                        nodes.remove(num)
                        print("Dropped node ", num)
                    else:
                        print("ERROR: Node", num, "does not exist")
                except:
                    print("ERROR: invalid integer ", func[1])
            elif (function0 == 'join'):
                try:
                    num1 = int(func[1])
                    num2 = int(func[2])
                    if (num1 and num2 in nodes):
                        SUCC = 'suc{}'.format(num1)
                        locals()[SUCC] = num2
                    else:
                        print("ERROR: Node", num1, "does not exist")

                except:
                    print("ERROR: invalid integer ", func[1])

            elif (function0 == 'stab'):
                try:
                    num = int(func[1])
                    if (num in nodes):
                        # print("Sorting NOdes")
                        sorted_nodes = np.sort(nodes)
                        count = -1
                        for i in sorted_nodes:
                            count = count + 1
                            if (i == num):
                                SUCC = 'suc{}'.format(i)
                                PRED = 'pred{}'.format(i)
                                if ((count + 1) >= len(nodes)):
                                    # print("last element after sorting")
                                    locals()[SUCC] = sorted_nodes[0]
                                else:
                                    # print("NOT last element after sorting")
                                    locals()[SUCC] = sorted_nodes[count + 1]
                                locals()[PRED] = sorted_nodes[count - 1]
                                break


                    else:

                        print("ERROR: Node", num, "does not exist")
                except:
                    print("ERROR: invalid integer ", func[1])
            elif (function0 == 'list'):
                for i in np.sort(nodes):
                    SUCC = 'suc{}'.format(i)
                    PRED = 'pred{}'.format(i)
                    FINGER = 'finger{}'.format(i)
                    arr = np.array(locals()[FINGER]['NodeId'])
                    print("Node :", i, " suc : ", locals()[SUCC], "pre : ", locals()[PRED], " fingers : ", arr)

            elif (function0 == 'fix'):

                try:

                    num = int(func[1])
                    FINGER = 'finger{}'.format(num)
                    # print("fixing")
                    # print(locals()[FINGER])
                    if (num in nodes):
                        sorted_array = np.sort(nodes)
                        for i in range(1, n + 1):
                            # print("Updating keys for index ", i)
                            d = num + np.power(2, i - 1)
                            if (d < max_key):
                                d = d

                            else:
                                d = d - max_key
                            locals()[FINGER].iloc[[i - 1], [1]] = d

                            e = num
                            for k in sorted_array:
                                if (k >= d):
                                    e = k
                                    break
                            locals()[FINGER].iloc[[i - 1], [2]] = e

                    else:

                        print("ERROR: Node", num, "does not exist")

                except:
                    print("ERROR: invalid integer ", func[1])
            elif (function0 == 'show'):

                try:
                    num = int(func[1])
                    if (num in nodes):
                        SUCC = 'suc{}'.format(num)
                        PRED = 'pred{}'.format(num)
                        FINGER = 'finger{}'.format(num)
                        arr = np.array(locals()[FINGER]['NodeId'])
                        print("Node :", num, " suc : ", locals()[SUCC], "pre : ", locals()[PRED], " fingers : ", arr)
                    else:
                        print("ERROR: Node", num, "does not exist")

                except:
                    print("ERROR: invalid integer ", func[1])
            else:
                print("Give correct function")
                continue

    except KeyboardInterrupt:
        pass

####################################################################################################################################################################################

elif (len(sys.argv) == 4):

    if (sys.argv[1] == "-i"):
        print("Batch mode")
        inp_file = sys.argv[2]
        f = open(inp_file, "r")

    else:
        print("Give arguments correctly")
        sys.exit(0)
    try:
        n = int(sys.argv[3])

        if (n < 1):
            print("The value of N should be greater than 1.")
            print("Program termintaing")
            sys.exit(0)

        max_key = np.power(2, n)
        keys_range = range(0, max_key)
        poss_keys = []
        for i in keys_range:
            poss_keys.append(i)

        n_keys = []
        for i in range(0, n):
            n_keys.append(i + 1)


    except:
        print("ERROR: invalid integer ", sys.argv[3])
    contents = f.readlines()
    # print(contents)

    for i in contents:

        func = i.split(" ")
        function0 = func[0]

        # print("Given : ", func)


        if (function0 == 'add'):
            try:
                num = int(func[1])

                if (num in nodes):
                    print("ERROR: Node", num, " exists")
                    continue
                else:
                    if (num in poss_keys):
                        nodes.append(num)
                        print("Added node ", num)
                        df = 'finger{}'.format(num)
                        locals()[df] = pd.DataFrame(columns=['No', 'keys', 'NodeId'])
                        locals()[df]['No'] = n_keys
                        locals()[df]['NodeId'] = num
                        predicissor = 'pred{}'.format(num)
                        locals()[predicissor] = 'none'
                        successor = 'suc{}'.format(num)
                        locals()[successor] = num






                    else:
                        print("ERROR: node id must be in [0,", max_key, ")")

                        continue
            except:
                print("ERROR: invalid integer ", func[1])

        elif (function0 == 'end\n'):

            sys.exit(1)
        elif (function0 == 'drop'):
            try:
                num = int(func[1])
                if (num in nodes):
                    nodes.remove(num)
                    print("Dropped node ", num)
                else:
                    print("ERROR: Node", num, "does not exist")
            except:
                print("ERROR: invalid integer ", func[1])
        elif (function0 == 'join'):
            try:
                num1 = int(func[1])
                num2 = int(func[2])
                if (num1 and num2 in nodes):
                    SUCC = 'suc{}'.format(num1)
                    locals()[SUCC] = num2
                else:
                    print("ERROR: Node", num1, "does not exist")

            except:
                print("ERROR: invalid integer ", func[1])

        elif (function0 == 'stab'):
            try:
                num = int(func[1])
                if (num in nodes):
                    # print("Sorting NOdes")
                    sorted_nodes = np.sort(nodes)
                    count = -1
                    for i in sorted_nodes:
                        count = count + 1
                        if (i == num):
                            SUCC = 'suc{}'.format(i)
                            PRED = 'pred{}'.format(i)
                            if ((count + 1) >= len(nodes)):
                                # print("last element after sorting")
                                locals()[SUCC] = sorted_nodes[0]
                            else:
                                # print("NOT last element after sorting")
                                locals()[SUCC] = sorted_nodes[count + 1]
                            locals()[PRED] = sorted_nodes[count - 1]
                            break


                else:

                    print("ERROR: Node", num, "does not exist")
            except:
                print("ERROR: invalid integer ", func[1])

        elif (function0 == 'list\n'):
            for i in np.sort(nodes):
                SUCC = 'suc{}'.format(i)
                PRED = 'pred{}'.format(i)
                FINGER = 'finger{}'.format(i)
                arr = np.array(locals()[FINGER]['NodeId'])
                print("Node :", i, " suc : ", locals()[SUCC], "pre : ", locals()[PRED], " fingers : ", arr)
        elif (function0 == 'fix'):
            try:

                num = int(func[1])
                FINGER = 'finger{}'.format(num)
                # print("fixing")
                # print(locals()[FINGER])
                if (num in nodes):
                    sorted_array = np.sort(nodes)
                    for i in range(1, n + 1):
                        # print("Updating keys for index ", i)
                        d = num + np.power(2, i - 1)
                        if (d < max_key):
                            d = d

                        else:
                            d = d - max_key
                        locals()[FINGER].iloc[[i - 1], [1]] = d

                        e = num
                        for k in sorted_array:
                            if (k >= d):
                                e = k
                                break
                        locals()[FINGER].iloc[[i - 1], [2]] = e

                else:

                    print("ERROR: Node", num, "does not exist")

            except:
                print("ERROR: invalid integer ", func[1])


        elif (function0 == 'show'):

            try:
                num = int(func[1])
                if (num in nodes):
                    SUCC = 'suc{}'.format(num)
                    PRED = 'pred{}'.format(num)
                    FINGER = 'finger{}'.format(num)
                    arr = np.array(locals()[FINGER]['NodeId'])
                    print("Node :", num, " suc : ", locals()[SUCC], "pre : ", locals()[PRED], " fingers : ", arr)
                else:
                    print("ERROR: Node", num, "does not exist")

            except:
                print("ERROR: invalid integer ", func[1])
        else:
            print("Give correct function")
            continue


else:
    print("BYE")












