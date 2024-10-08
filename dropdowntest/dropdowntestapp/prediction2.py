import requests
import numpy as np

# Prompt the user to enter the names of the home team and away team
# home_team_name = input("Enter the name of the home team: ")
# away_team_name = input("Enter the name of the away team: ")

api_key = "68edaca6-04ed-4695-9216-a383dabb4964"
num = 16
minimum = 1
maximum = 100
base = 10
format_ = "plain"
url = f"https://www.random.org/integers/?num={num}&min={minimum}&max={maximum}&col=1&base={base}" \
      f"&format={format_}&rnd=new&key={api_key}"


def predict_winner(home_team_name, away_team_name):
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            random_numbers = response.text.split()
            random_matrix = np.array(random_numbers).astype(int).reshape(4, 4).T

            print("Generated random numbers:")
            print(random_matrix)

            # Space
            print("")

            # Convert odd numbers to 1 and even numbers to 0
            random_matrix = np.where(random_matrix % 2 == 0, 0, 1)
            print("Converted random numbers:")
            print(random_matrix)

            # Space
            print("")

            # Create Transpose of the original matrix
            child_matrix = np.transpose(random_matrix)
            print("Transposed matrix:")
            print(child_matrix)

            # Space
            print("")

            # Create concatenated figures from the random_matrix and child matrix
            print("Parent figures")
            H1 = "".join([str(random_matrix[i][0]) for i in range(len(random_matrix))])
            print("H1 =", H1)
            H2 = "".join([str(random_matrix[i][1]) for i in range(len(random_matrix))])
            print("H2 =", H2)
            H3 = "".join([str(random_matrix[i][2]) for i in range(len(random_matrix))])
            print("H3 =", H3)
            H4 = "".join([str(random_matrix[i][3]) for i in range(len(random_matrix))])
            print("H4 =", H4)

            # Space
            print("")

            print("Children figures")
            H5 = "".join([str(child_matrix[i][0]) for i in range(len(child_matrix))])
            print("H5 =", H5)
            H6 = "".join([str(child_matrix[i][1]) for i in range(len(child_matrix))])
            print("H6 =", H6)
            H7 = "".join([str(child_matrix[i][2]) for i in range(len(child_matrix))])
            print("H7 =", H7)
            H8 = "".join([str(child_matrix[i][3]) for i in range(len(child_matrix))])
            print("H8 =", H8)

            # Space
            print("")

            # Generate grandchildren and great-grandchildren
            # Extract values from the matrix by indexing it using the row and column numbers.
            R1C1 = random_matrix[0][0]  # Row 1, Column 1
            R1C2 = random_matrix[0][1]  # Row 1, Column 2

            if R1C1 == 1 and R1C2 == 0:
                H91 = 1
            elif R1C1 == 0 and R1C2 == 1:
                H91 = 1
            elif R1C1 == 1 and R1C2 == 1:
                H91 = 0
            else:
                H91 = 0
            print("Grandchildren matrix figures")
            # print("H91 =", H91)

            R2C1 = random_matrix[1][0]  # Row 2, Column 1
            R2C2 = random_matrix[1][1]  # Row 2, Column 2

            if R2C1 == 1 and R2C2 == 0:
                H92 = 1
            elif R2C1 == 0 and R2C2 == 1:
                H92 = 1
            elif R2C1 == 1 and R2C2 == 1:
                H92 = 0
            else:
                H92 = 0
            # print("H92 =", H92)

            R3C1 = random_matrix[2][0]  # Row 3, Column 1
            R3C2 = random_matrix[2][1]  # Row 3, Column 2

            if R3C1 == 1 and R3C2 == 0:
                H93 = 1
            elif R3C1 == 0 and R3C2 == 1:
                H93 = 1
            elif R3C1 == 1 and R3C2 == 1:
                H93 = 0
            else:
                H93 = 0
            # print("H93 =", H93)

            R4C1 = random_matrix[3][0]  # Row 4, Column 1
            R4C2 = random_matrix[3][1]  # Row 4, Column 2

            if R4C1 == 1 and R4C2 == 0:
                H94 = 1
            elif R4C1 == 0 and R4C2 == 1:
                H94 = 1
            elif R4C1 == 1 and R4C2 == 1:
                H94 = 0
            else:
                H94 = 0
            # print("H94 =", H94)

            H9 = int(str(H91) + str(H92) + str(H93) + str(H94))
            H9_str = '{:04d}'.format(H9)
            print("H9 =", H9_str)
            # print("H9 =", H9)

            # Space
            print("")

            R1C3 = random_matrix[0][2]  # Row 1, Column 3
            R1C4 = random_matrix[0][3]  # Row 1, Column 4

            if R1C3 == 1 and R1C4 == 0:
                H101 = 1
            elif R1C3 == 0 and R1C4 == 1:
                H101 = 1
            elif R1C3 == 1 and R1C4 == 1:
                H101 = 0
            else:
                H101 = 0
            # print("H101 =", H101)

            R2C3 = random_matrix[1][2]  # Row 2, Column 3
            R2C4 = random_matrix[1][3]  # Row 2, Column 4

            if R2C3 == 1 and R2C4 == 0:
                H102 = 1
            elif R2C3 == 0 and R2C4 == 1:
                H102 = 1
            elif R2C3 == 1 and R2C4 == 1:
                H102 = 0
            else:
                H102 = 0
            # print("H102 =", H102)

            R3C3 = random_matrix[2][2]  # Row 3, Column 3
            R3C4 = random_matrix[2][3]  # Row 3, Column 4

            if R3C3 == 1 and R3C4 == 0:
                H103 = 1
            elif R3C3 == 0 and R3C4 == 1:
                H103 = 1
            elif R3C3 == 1 and R3C4 == 1:
                H103 = 0
            else:
                H103 = 0
            # print("H103 =", H103)

            R4C3 = random_matrix[3][2]  # Row 4, Column 3
            R4C4 = random_matrix[3][3]  # Row 4, Column 4

            if R4C3 == 1 and R4C4 == 0:
                H104 = 1
            elif R4C3 == 0 and R4C4 == 1:
                H104 = 1
            elif R4C3 == 1 and R4C4 == 1:
                H104 = 0
            else:
                H104 = 0
            # print("H104 =", H104)

            H10 = int(str(H101) + str(H102) + str(H103) + str(H104))
            H10_str = '{:04d}'.format(H10)
            print("H10 =", H10_str)
            # print("H10 =", H10)
            # Space
            print("")

            RR1CC1 = child_matrix[0][0]  # Row 1, Column 1
            RR1CC2 = child_matrix[0][1]  # Row 1, Column 2

            if RR1CC1 == 1 and RR1CC2 == 0:
                H111 = 1
            elif RR1CC1 == 0 and RR1CC2 == 1:
                H111 = 1
            elif RR1CC1 == 1 and RR1CC2 == 1:
                H111 = 0
            else:
                H111 = 0
            # print("H111 =", H111)

            RR2CC1 = child_matrix[1][0]  # Row 2, Column 1
            RR2CC2 = child_matrix[1][1]  # Row 2, Column 2

            if RR2CC1 == 1 and RR2CC2 == 0:
                H112 = 1
            elif RR2CC1 == 0 and RR2CC2 == 1:
                H112 = 1
            elif RR2CC1 == 1 and RR2CC2 == 1:
                H112 = 0
            else:
                H112 = 0
            # print("H112 =", H112)

            RR3CC1 = child_matrix[2][0]  # Row 3, Column 1
            RR3CC2 = child_matrix[2][1]  # Row 3, Column 2

            if RR3CC1 == 1 and RR3CC2 == 0:
                H113 = 1
            elif RR3CC1 == 0 and RR3CC2 == 1:
                H113 = 1
            elif RR3CC1 == 1 and RR3CC2 == 1:
                H113 = 0
            else:
                H113 = 0
            # print("H113 =", H113)

            RR4CC1 = child_matrix[3][0]  # Row 4, Column 1
            RR4CC2 = child_matrix[3][1]  # Row 4, Column 2

            if RR4CC1 == 1 and RR4CC2 == 0:
                H114 = 1
            elif RR4CC1 == 0 and RR4CC2 == 1:
                H114 = 1
            elif RR4CC1 == 1 and RR4CC2 == 1:
                H114 = 0
            else:
                H114 = 0
            # print("H114 =", H114)

            H11 = int(str(H111) + str(H112) + str(H113) + str(H114))
            H11_str = '{:04d}'.format(H11)
            print("H11 =", H11_str)
            # print("H11 =", H11)
            # Space
            print("")

            RR1CC3 = child_matrix[0][2]  # Row 1, Column 3
            RR1CC4 = child_matrix[0][3]  # Row 1, Column 4

            if RR1CC3 == 1 and RR1CC4 == 0:
                H121 = 1
            elif RR1CC3 == 0 and RR1CC4 == 1:
                H121 = 1
            elif RR1CC3 == 1 and RR1CC4 == 1:
                H121 = 0
            else:
                H121 = 0
            # print("H121 =", H121)

            RR2CC3 = child_matrix[1][2]  # Row 2, Column 3
            RR2CC4 = child_matrix[1][3]  # Row 2, Column 4

            if RR2CC3 == 1 and RR2CC4 == 0:
                H122 = 1
            elif RR2CC3 == 0 and RR2CC4 == 1:
                H122 = 1
            elif RR2CC3 == 1 and RR2CC4 == 1:
                H122 = 0
            else:
                H122 = 0
            # print("H122 =", H122)

            RR3CC3 = child_matrix[2][2]  # Row 3, Column 3
            RR3CC4 = child_matrix[2][3]  # Row 3, Column 4

            if RR3CC3 == 1 and RR3CC4 == 0:
                H123 = 1
            elif RR3CC3 == 0 and RR3CC4 == 1:
                H123 = 1
            elif RR3CC3 == 1 and RR3CC4 == 1:
                H123 = 0
            else:
                H123 = 0
            # print("H123 =", H123)

            RR4CC3 = child_matrix[3][2]  # Row 4, Column 3
            RR4CC4 = child_matrix[3][3]  # Row 4, Column 4

            if RR4CC3 == 1 and RR4CC4 == 0:
                H124 = 1
            elif RR4CC3 == 0 and RR4CC4 == 1:
                H124 = 1
            elif RR4CC3 == 1 and RR4CC4 == 1:
                H124 = 0
            else:
                H124 = 0
            # print("H124 =", H124)

            H12 = int(str(H121) + str(H122) + str(H123) + str(H124))
            H12_str = '{:04d}'.format(H12)
            print("H12 =", H12_str)
            # print("H12 =", H12)
            # Space
            print("")

            # Generate H13. Use H9 and H10.

            if H91 == 1 and H101 == 0:
                H131 = 1
            elif H91 == 0 and H101 == 1:
                H131 = 1
            elif H91 == 1 and H101 == 1:
                H131 = 0
            else:
                H131 = 0
            # print("H131 =", H131)

            if H92 == 1 and H102 == 0:
                H132 = 1
            elif H92 == 0 and H102 == 1:
                H132 = 1
            elif H92 == 1 and H102 == 1:
                H132 = 0
            else:
                H132 = 0
            # print("H132 =", H132)

            if H93 == 1 and H103 == 0:
                H133 = 1
            elif H93 == 0 and H103 == 1:
                H133 = 1
            elif H93 == 1 and H103 == 1:
                H133 = 0
            else:
                H133 = 0
            # print("H133 =", H133)

            if H94 == 1 and H104 == 0:
                H134 = 1
            elif H94 == 0 and H104 == 1:
                H134 = 1
            elif H94 == 1 and H104 == 1:
                H134 = 0
            else:
                H134 = 0
            # print("H134 =", H134)

            H13 = int(str(H131) + str(H132) + str(H133) + str(H134))
            H13_str = '{:04d}'.format(H13)
            print("H13 =", H13_str)
            # print("H13 =", H13)
            # Space
            print("")

            # Generate H14. Use H11 and H12.

            if H111 == 1 and H121 == 0:
                H141 = 1
            elif H111 == 0 and H121 == 1:
                H141 = 1
            elif H111 == 1 and H121 == 1:
                H141 = 0
            else:
                H141 = 0
            # print("H141 =", H141)

            if H112 == 1 and H122 == 0:
                H142 = 1
            elif H112 == 0 and H122 == 1:
                H142 = 1
            elif H112 == 1 and H122 == 1:
                H142 = 0
            else:
                H142 = 0
            # print("H142 =", H142)

            if H113 == 1 and H123 == 0:
                H143 = 1
            elif H113 == 0 and H123 == 1:
                H143 = 1
            elif H113 == 1 and H123 == 1:
                H143 = 0
            else:
                H143 = 0
            # print("H143 =", H143)

            if H114 == 1 and H124 == 0:
                H144 = 1
            elif H114 == 0 and H124 == 1:
                H144 = 1
            elif H114 == 1 and H124 == 1:
                H144 = 0
            else:
                H144 = 0
            # print("H144 =", H144)

            H14 = int(str(H141) + str(H142) + str(H143) + str(H144))
            H14_str = '{:04d}'.format(H14)
            print("H14 =", H14_str)
            # print("H14 =", H14)
            # Space
            print("")

            # Generate H15. Use H13 and H14.

            if H131 == 1 and H141 == 0:
                H151 = 1
            elif H131 == 0 and H141 == 1:
                H151 = 1
            elif H131 == 1 and H141 == 1:
                H151 = 0
            else:
                H151 = 0
            # print("H151 =", H151)

            if H132 == 1 and H142 == 0:
                H152 = 1
            elif H132 == 0 and H142 == 1:
                H152 = 1
            elif H132 == 1 and H142 == 1:
                H152 = 0
            else:
                H152 = 0
            # print("H152 =", H152)

            if H133 == 1 and H143 == 0:
                H153 = 1
            elif H133 == 0 and H143 == 1:
                H153 = 1
            elif H133 == 1 and H143 == 1:
                H153 = 0
            else:
                H153 = 0
            # print("H153 =", H153)

            if H134 == 1 and H144 == 0:
                H154 = 1
            elif H134 == 0 and H144 == 1:
                H154 = 1
            elif H134 == 1 and H144 == 1:
                H154 = 0
            else:
                H154 = 0
            # print("H154 =", H154)

            H15 = int(str(H151) + str(H152) + str(H153) + str(H154))
            H15_str = '{:04d}'.format(H15)
            print("H15 =", H15_str)
            # print("H15 =", H15)
            # Space
            print("")

            # Generate H16. Use H15 and H1.

            if H151 == 1 and R1C1 == 0:
                H161 = 1
            elif H151 == 0 and R1C1 == 1:
                H161 = 1
            elif H151 == 1 and R1C1 == 1:
                H161 = 0
            else:
                H161 = 0
            # print("H161 =", H161)

            if H152 == 1 and R2C1 == 0:
                H162 = 1
            elif H152 == 0 and R2C1 == 1:
                H162 = 1
            elif H152 == 1 and R2C1 == 1:
                H162 = 0
            else:
                H162 = 0
            # print("H162 =", H162)

            if H153 == 1 and R3C1 == 0:
                H163 = 1
            elif H153 == 0 and R3C1 == 1:
                H163 = 1
            elif H153 == 1 and R3C1 == 1:
                H163 = 0
            else:
                H163 = 0
            # print("H163 =", H163)

            if H154 == 1 and R4C1 == 0:
                H164 = 1
            elif H154 == 0 and R4C1 == 1:
                H164 = 1
            elif H154 == 1 and R4C1 == 1:
                H164 = 0
            else:
                H164 = 0
            # print("H164 =", H164)

            H16 = int(str(H161) + str(H162) + str(H163) + str(H164))
            H16_str = '{:04d}'.format(H16)
            print("H16 =", H16_str)
            # print("H16 =", H16)
            # Space
            print("")

            # CHECKS
            print("BASIC CHECKS")

            # Space
            print("")

            # Check Reliability of chart
            # calculate the sum of H151, H152, H153, and H154, call the answer sum_15
            sum_15 = H151 + H152 + H153 + H154
            # print("Sum of H15 =", sum_15)
            # check if the sum is 0, 2, or 4
            if sum_15 == 0 or sum_15 == 2 or sum_15 == 4:
                print("Chart is Reliable")
            else:
                print("Chart is Not Reliable")

            # create variables for "Chart is Reliable" and "Chart is Not Reliable"
            # cr = "Chart is Reliable"
            # cnr = "Chart is Not Reliable"

            # Space
            print("")

            # Check Validity of chart (H3 X H5) = jar; (H11 X H15) = hi; (jar x hi) = Valid
            # Jar
            if R1C3 == 1 and RR1CC1 == 0:
                jar1 = 1
            elif R1C3 == 0 and RR1CC1 == 1:
                jar1 = 1
            elif R1C3 == 1 and RR1CC1 == 1:
                jar1 = 0
            else:
                jar1 = 0
            # print("jar1 =", jar1)

            if R2C3 == 1 and RR2CC1 == 0:
                jar2 = 1
            elif R2C3 == 0 and RR2CC1 == 1:
                jar2 = 1
            elif R2C3 == 1 and RR2CC1 == 1:
                jar2 = 0
            else:
                jar2 = 0
            # print("jar2 =", jar2)

            if R3C3 == 1 and RR3CC1 == 0:
                jar3 = 1
            elif R3C3 == 0 and RR3CC1 == 1:
                jar3 = 1
            elif R3C3 == 1 and RR3CC1 == 1:
                jar3 = 0
            else:
                jar3 = 0
            # print("jar3 =", jar3)

            if R4C3 == 1 and RR4CC1 == 0:
                jar4 = 1
            elif R4C3 == 0 and RR4CC1 == 1:
                jar4 = 1
            elif R4C3 == 1 and RR4CC1 == 1:
                jar4 = 0
            else:
                jar4 = 0
            # print("jar4 =", jar4)

            jar = int(str(jar1) + str(jar2) + str(jar3) + str(jar4))
            jar_str = '{:04d}'.format(jar)
            # print("jar =", jar_str)

            # Space
            # print("")

            # Hi
            if H111 == 1 and H151 == 0:
                hi1 = 1
            elif H111 == 0 and H151 == 1:
                hi1 = 1
            elif H111 == 1 and H151 == 1:
                hi1 = 0
            else:
                hi1 = 0
            # print("hi1 =", hi1)

            if H112 == 1 and H152 == 0:
                hi2 = 1
            elif H112 == 0 and H152 == 1:
                hi2 = 1
            elif H112 == 1 and H152 == 1:
                hi2 = 0
            else:
                hi2 = 0
            # print("hi2 =", hi2)

            if H113 == 1 and H153 == 0:
                hi3 = 1
            elif H113 == 0 and H153 == 1:
                hi3 = 1
            elif H113 == 1 and H153 == 1:
                hi3 = 0
            else:
                hi3 = 0
            # print("hi3 =", hi3)

            if H114 == 1 and H154 == 0:
                hi4 = 1
            elif H114 == 0 and H154 == 1:
                hi4 = 1
            elif H114 == 1 and H154 == 1:
                hi4 = 0
            else:
                hi4 = 0
            # print("hi4 =", hi4)

            hi = int(str(hi1) + str(hi2) + str(hi3) + str(hi4))
            hi_str = '{:04d}'.format(hi)
            # print("hi =", hi_str)

            # Space
            # print("")

            # Valid
            if jar1 == 1 and hi1 == 0:
                valid1 = 1
            elif jar1 == 0 and hi1 == 1:
                valid1 = 1
            elif jar1 == 1 and hi1 == 1:
                valid1 = 0
            else:
                valid1 = 0
            # print("valid1 =", valid1)

            if jar2 == 1 and hi2 == 0:
                valid2 = 1
            elif jar2 == 0 and hi2 == 1:
                valid2 = 1
            elif jar2 == 1 and hi2 == 1:
                valid2 = 0
            else:
                valid2 = 0
            # print("valid2 =", valid2)

            if jar3 == 1 and hi3 == 0:
                valid3 = 1
            elif jar3 == 0 and hi3 == 1:
                valid3 = 1
            elif jar3 == 1 and hi3 == 1:
                valid3 = 0
            else:
                valid3 = 0
            # print("valid3 =", valid3)

            if jar4 == 1 and hi4 == 0:
                valid4 = 1
            elif jar4 == 0 and hi4 == 1:
                valid4 = 1
            elif jar4 == 1 and hi4 == 1:
                valid4 = 0
            else:
                valid4 = 0
            # print("valid4 =", valid4)

            valid = int(str(valid1) + str(valid2) + str(valid3) + str(valid4))
            valid_str = '{:04d}'.format(valid)
            # print("valid =", valid_str)

            # Space
            # print("")

            # Check if valid_str matches any of H1, H2, H3 ... H16
            if valid_str in [H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12, H13, H14, H15, H16]:
                print("Chart is Valid")

                # Check sincerity of user
                # Create a variable sincere to compute Sincerity
                # sincere = (H1 + H9 + H10 + H13 + 9) % 16
                # Compute the sum of H1
                H1_sum = 0
                if R1C1 == 0:
                    H1_sum += 2
                else:
                    H1_sum += 1

                if R2C1 == 0:
                    H1_sum += 2
                else:
                    H1_sum += 1

                if R3C1 == 0:
                    H1_sum += 2
                else:
                    H1_sum += 1

                if R4C1 == 0:
                    H1_sum += 2
                else:
                    H1_sum += 1

                # Print the sum of H1
                # print("H1_sum =", H1_sum)

                # Compute the sum of H9
                H9_sum = 0
                if H91 == 0:
                    H9_sum += 2
                else:
                    H9_sum += 1

                if H92 == 0:
                    H9_sum += 2
                else:
                    H9_sum += 1

                if H93 == 0:
                    H9_sum += 2
                else:
                    H9_sum += 1

                if H94 == 0:
                    H9_sum += 2
                else:
                    H9_sum += 1

                # Print the sum of H9
                # print("H9_sum =", H9_sum)

                # Compute the sum of H10
                H10_sum = 0
                if H101 == 0:
                    H10_sum += 2
                else:
                    H10_sum += 1

                if H102 == 0:
                    H10_sum += 2
                else:
                    H10_sum += 1

                if H103 == 0:
                    H10_sum += 2
                else:
                    H10_sum += 1

                if H104 == 0:
                    H10_sum += 2
                else:
                    H10_sum += 1

                # Print the sum of H10
                # print("H10_sum =", H10_sum)

                # Compute the sum of H13
                H13_sum = 0
                if H131 == 0:
                    H13_sum += 2
                else:
                    H13_sum += 1

                if H132 == 0:
                    H13_sum += 2
                else:
                    H13_sum += 1

                if H133 == 0:
                    H13_sum += 2
                else:
                    H13_sum += 1

                if H134 == 0:
                    H13_sum += 2
                else:
                    H13_sum += 1

                # Print the sum of H13
                # print("H13_sum =", H13_sum)

                sincere = (H1_sum + H9_sum + H10_sum + H13_sum + 9) % 16

                # Sincere is the remainder of the above computation which ranges from 0 to 15.
                # Print the remainder
                print("sincere = ", sincere)

                if sincere == 1:
                    sum_H1 = R1C1 + R2C1 + R3C1 + R4C1
                    if sum_H1 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 2:
                    sum_H2 = R1C2 + R2C2 + R3C2 + R4C2
                    if sum_H2 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 3:
                    sum_H3 = R1C3 + R2C3 + R3C3 + R4C3
                    if sum_H3 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 4:
                    sum_H4 = R1C4 + R2C4 + R3C4 + R4C4
                    if sum_H4 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 5:
                    sum_H5 = RR1CC1 + RR2CC1 + RR3CC1 + RR4CC1
                    if sum_H5 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 6:
                    sum_H6 = RR1CC2 + RR2CC2 + RR3CC2 + RR4CC2
                    if sum_H6 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 7:
                    sum_H7 = RR1CC3 + RR2CC3 + RR3CC3 + RR4CC3
                    if sum_H7 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 8:
                    sum_H8 = RR1CC4 + RR2CC4 + RR3CC4 + RR4CC4
                    if sum_H8 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 9:
                    sum_H9 = H91 + H92 + H93 + H94
                    if sum_H9 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 10:
                    sum_H10 = H101 + H102 + H103 + H104
                    if sum_H10 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 11:
                    sum_H11 = H111 + H112 + H113 + H114
                    if sum_H11 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 12:
                    sum_H12 = H121 + H122 + H123 + H124
                    if sum_H12 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 13:
                    sum_H13 = H131 + H132 + H133 + H134
                    if sum_H13 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 14:
                    sum_H14 = H141 + H142 + H143 + H144
                    if sum_H14 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 15:
                    sum_H15 = H151 + H152 + H153 + H154
                    if sum_H15 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                elif sincere == 0:
                    sum_H16 = H161 + H162 + H163 + H164
                    if sum_H16 in [0, 2, 4]:
                        print("Sincere")

                        # Formula 1
                        # Compare number of times 0011, 0111, 0101, 0010, 1100, 1000, 0110, 1111 or 1101 \
                        # occurs for Home and Away teams
                        # Binary numbers were converted to base 10 for ease of comparison
                        # Convert H1 to H16 to base 10
                        h1 = int(H1, 2)
                        h2 = int(H2, 2)
                        h3 = int(H3, 2)
                        h4 = int(H4, 2)
                        h5 = int(H5, 2)
                        h6 = int(H6, 2)
                        h7 = int(H7, 2)
                        h8 = int(H8, 2)
                        h9 = int(str(H9), 2)
                        h10 = int(str(H10), 2)
                        h11 = int(str(H11), 2)
                        h12 = int(str(H12), 2)
                        h13 = int(str(H13), 2)
                        h14 = int(str(H14), 2)
                        h15 = int(str(H15), 2)
                        h16 = int(str(H16), 2)

                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        hm_total = 0

                        # Checking h1
                        if h1 in values_to_check:
                            hm_total += 1

                        # Checking h3
                        if h3 in values_to_check:
                            hm_total += 1

                        # Checking h5
                        if h5 in values_to_check:
                            hm_total += 1

                        # Checking h7
                        if h7 in values_to_check:
                            hm_total += 1

                        # Checking h9
                        if h9 in values_to_check:
                            hm_total += 1

                        # Checking h11
                        if h11 in values_to_check:
                            hm_total += 1

                        # Checking h13
                        if h13 in values_to_check:
                            hm_total += 1

                        # Checking h15
                        if h15 in values_to_check:
                            hm_total += 1

                        # print("hm_total:", hm_total)

                        # For away team.
                        values_to_check = [3, 7, 5, 2, 12, 8, 6, 15, 13]
                        aw_total = 0

                        # Checking h2
                        if h2 in values_to_check:
                            aw_total += 1

                        # Checking h4
                        if h4 in values_to_check:
                            aw_total += 1

                        # Checking h6
                        if h6 in values_to_check:
                            aw_total += 1

                        # Checking h8
                        if h8 in values_to_check:
                            aw_total += 1

                        # Checking h10
                        if h10 in values_to_check:
                            aw_total += 1

                        # Checking h12
                        if h12 in values_to_check:
                            aw_total += 1

                        # Checking h14
                        if h14 in values_to_check:
                            aw_total += 1

                        # Checking h16
                        if h16 in values_to_check:
                            aw_total += 1

                        # print("aw_total:", aw_total)

                        result_method1 = None
                        if hm_total > aw_total:
                            result_method1 = f"{home_team_name} will Win"
                        elif aw_total > hm_total:
                            result_method1 = f"{away_team_name} will Win"
                        else:
                            result_method1 = "It will be a draw"

                        print("result_method1:", result_method1)

                        # Formula 2
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [5, 7, 3],  # Class 1
                            [2],  # Class 2
                            [8, 12],  # Class 3
                            [6],  # Class 4
                            [15, 13],  # Class 5
                            [0],  # Class 6
                            [11, 9],  # Class 7
                            [10, 14],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method2 = None
                        if h1_class < h7_class:
                            result_method2 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method2 = f"{away_team_name} will Win"
                        else:
                            result_method2 = "It will be a draw"
                        print("result_method2:", result_method2)

                        # Formula 3
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 7],  # Class 1
                            [6, 2],  # Class 2
                            [11],  # Class 3
                            [12, 8],  # Class 4
                            [0],  # Class 5
                            [9, 15],  # Class 6
                            [10, 14],  # Class 7
                            [13],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]
                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method3 = None
                        if h1_class < h7_class:
                            result_method3 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method3 = f"{away_team_name} will Win"
                        else:
                            result_method3 = "It will be a draw"
                        print("result_method3:", result_method3)

                        # Formula 4
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 6.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 5, 8, 2],  # Class 1
                            [6, 12, 7],  # Class 2
                            [11],  # Class 3
                            [0, 9, 15],  # Class 4
                            [10, 4, 13, 14],  # Class 5
                            [1],  # Class 6
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method4 = None
                        if h1_class < h7_class:
                            result_method4 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method4 = f"{away_team_name} will Win"
                        else:
                            result_method4 = "It will be a draw"
                        print("result_method4:", result_method4)

                        # Formula 5
                        # Compare figure in h1 (Home team) with h7 (Away team) using a standard defined as classes 1 to 10.
                        # Binary numbers were converted to base 10 for ease of comparison

                        # Define the classes
                        classes = [
                            [3, 7, 5],  # Class 1
                            [12],  # Class 2
                            [6, 2],  # Class 3
                            [11],  # Class 4
                            [8],  # Class 5
                            [0],  # Class 6
                            [15, 13, 9],  # Class 7
                            [14, 10],  # Class 8
                            [4],  # Class 9
                            [1],  # Class 10
                        ]

                        # Define figures to compare
                        h1 = int(H1, 2)
                        h7 = int(H7, 2)

                        # Find the classes that contain h1 and h7
                        h1_class = None
                        h7_class = None
                        for i, c in enumerate(classes):
                            if h1 in c:
                                h1_class = i + 1
                            if h7 in c:
                                h7_class = i + 1

                        # Compare the classes and determine the winner
                        result_method5 = None
                        if h1_class < h7_class:
                            result_method5 = f"{home_team_name} will Win"
                        elif h7_class < h1_class:
                            result_method5 = f"{away_team_name} will Win"
                        else:
                            result_method5 = "It will be a draw"
                        print("result_method5:", result_method5)

                        # Determine the final result based on the results of the five methods
                        results = [result_method1, result_method2, result_method3, result_method4, result_method5]

                        home_win_text = f"{home_team_name} will Win"
                        away_win_text = f"{away_team_name} will Win"
                        draw_text = "It will be a draw"

                        home_wins = results.count(home_win_text)
                        away_wins = results.count(away_win_text)
                        draws = results.count(draw_text)

                        if home_wins >= 3:
                            final_result = f"{home_team_name} will win"
                        elif away_wins >= 3:
                            final_result = f"{away_team_name} will win"
                        elif draws >= 3:
                            final_result = "It will be a draw"
                        else:
                            final_result = "Sorry, we cannot determine the winner of this match"

                        print(final_result)

                    else:
                        print("Not Sincere...")

                break
            else:
                print("Chart is Not Valid. Fetching new random numbers")

        except requests.RequestException as e:
            print(f"Oops! An error occurred: {e}")
            print("Unable to fetch random numbers from the API.")
            # break
            return "Unable to fetch random numbers from the API."
