# Git Assignment - HeroVired

## Overview
This repository contains Python scripts for various computational tasks, including arithmetic operations, geometric calculations, and Git version control workflows. It is part of the Git assignment for HeroVired, demonstrating version control best practices, collaboration, and branching strategies.

## Repository Structure
- **calculator.py**: A Python script that performs basic arithmetic operations, including addition, subtraction, multiplication, division, square root function along with performing geometric calculations, including area computations for circles and rectangles.
- **git_lfs.txt**: A text file having detailed steps for Git LFS tracking.
- **large_file.bin**: A large binary file tracked using Git LFS.
- **.gitattributes:** A Git configuration file that specifies how certain files should be handled by Git LFS.
- **README.md**: This file, providing details about the repository.

## Branches Overview
- **main**: The primary branch containing stable releases.
- **dev**: A development branch where new features and bug fixes are tested before merging into main.
- **lfs**: A branch dedicated to handling large files using Git LFS.
- **feature/sqrt**: A branch for implementing the square root function in "calculator.py".
- **geometry-calculator**: Serves as the main feature branch where different sub-features (circle area and rectangle area calculations) are developed and merged.
- **feature/circle-area**: A branch for implementing the area calculation of a circle in "calculator.py".
- **feature/rectangle-area**: A branch for implementing the area calculation of a rectangle in "calculator.py".
   
## Workflow Steps

### **1️⃣CalculatorPlus Implementation**
1. **Create the Repository**
   - Create a GitHub repository named `git_assignment_HeroVired` and clone it locally.

2. **Create a Development Branch and add the provided code**
   - Switch to the `dev` branch.

3. **Merge with Main and Release Version 1**
   - Merge `dev` into `main` and create a v1.0 release.
   - Add any of your classmates as collaborators.

4. **Implement Square Root Feature**
   - Create a new branch `feature/sqrt` and implement the square root function.
   - Uncomment and implement the `square_root` function in `calculator.py`.
   - Commit your changes in the local branch `feature/sqrt`.

5. **Bug Fixation**
   - Switch to the `dev` branch.
   - Modify the `divide` function to prevent division by zero.
   - Implement the fix in the `dev` branch and merge it.
   - Create a pull request to push the changes to the `main` branch from `dev`.

6. **Feature Addition and Release Version 2**
   - Switch to the `feature/sqrt` branch.
   - Merge the updated changes from `dev` branch to `feature/sqrt` branch and fix the conflicts if any.
   - Create a pull request to push the changes to the `feature/sqrt` branch from `dev`.
   - Merge `dev` into `main` and create a v2.0 release.

### **2️⃣Handling Large Files with Git LFS**
1. **Create a Branch for Git LFS**
   - Switch to a new branch `lfs`:
     ```sh
     git checkout -b lfs
     ```
2. **Install and Set Up Git LFS**<br>
   - Download and install the Git command line extension. 
     ```sh
     https://github.com/git-lfs/git-lfs/releases/download/v3.6.1/git-lfs-windows-v3.6.1.exe
     ```
   - Once downloaded and installed, set up Git LFS for your user account and select the file types you'd like Git LFS to manage (or directly edit your .gitattributes)
     ```sh
     git lfs install
     git lfs track "*.bin"
     git add .gitattributes
     ```
3. **Upload Large Files ans Push Features**
   - Add and commit a file over 200MB.
   - Implement, commit, and push all the changes or requirements into the current branch.
     ```sh
     git add .
     git commit -m "Add .bin file"
     git push origin lfs
     ```
   - Merge into `main` once you are done.

### **3️⃣Geometry Calculator with Git Stash**
1. **Create a main feature branch geometry-calculator**
   - Switch to the `geometry-calculator` branch.
     
2. **Create Feature Branches from the main feature branch "geometry-calculator"**
   - `feature/circle-area` for circle area calculations.
   - `feature/rectangle-area` for rectangle area calculations.

3. **Use Git Stash**
   - Before switching branches, stash incomplete changes:
     ```sh
     git stash
     ```
   - Retrieve the stashed changes when resuming work:
     ```sh
     git stash pop
     ```

4. **Commit and Push Features**
   - Implement, commit, and push both features.
   - Create pull requests for `dev`.
   - Merge into `main` upon approval.

## Contribution
To contribute:
1. Fork the repository.
2. Create a feature branch from the dev branch.
3. Commit your changes.
4. Push to your branch and open a Pull Request.

## Scripts Execution steps with Output Screenshots reference
- calculator.py Output [Question 1]
``` sh
python calculator_plus.py 
```
![image](https://github.com/user-attachments/assets/afa33ace-1c25-4c1e-8838-cacde74301a2)

- git lsf output [Question 2]
```sh
  git lfs ls-files
```
![image](https://github.com/user-attachments/assets/01f55558-c4bf-43fd-b5fd-6ffc21ff6c8a)

- calculator.py Output [Question 3]
``` sh
python calculator_plus.py 
```
![image](https://github.com/user-attachments/assets/45defd47-6de4-400f-91d0-d1654ae2b487)
![image](https://github.com/user-attachments/assets/056a11c5-0e24-4428-b86b-626a9a463bac)
![image](https://github.com/user-attachments/assets/1ff62265-b606-428f-ab5f-53827cd49343)
![image](https://github.com/user-attachments/assets/a77ceffe-4c3f-420b-897e-b3e225cdd026)
![image](https://github.com/user-attachments/assets/044e475d-2523-41c1-8565-5b2d88ca08da)

- Output post changes implementation as per the feedback [Question 3]
```sh
1. Try-except blocks to handle invalid inputs and errors like division by zero or square root of negative numbers.
2. User input instead of hardcoded values.
3. Formatted results to 2 decimal places for better readability.
```
![image](https://github.com/user-attachments/assets/889c57ea-5a03-4e9e-bf18-c78c24df18c6)


## License
This project is for educational purposes and does not have a specific license.

## Get in Touch
Have any questions or suggestions? I'd love to hear from you! Feel free to reach out:<br>
📧 Email: tanujbhatia0001@gmail.com<br>
Looking forward to connecting! 🚀

