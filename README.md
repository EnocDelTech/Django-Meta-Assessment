# Little Lemon App


## Main Steps
1. **Create an environment:**

    **Windows:**
    ```
    python -m venv env
    ```
    **MacOS:**
    ```
    python3 -m venv env
    ```

2. **Environment activate:**

    **Windows:**
    ```
    .\env\Scripts\activate
    ```
    **MacOS:**
    ```
    source env/bin/activate
    ```

3. **Install Django:**

    **Windows:**
    ```
    pip install django
    ```
    **MacOS:**
    ```
    pip3 install django
    ```

    **Verify Django Version:**

    **Windows:**
    ```
    python -m django version
    ```
    **MacOS:**
    ```
    python3 -m django version
    ```

4. **Start Project:**

    ```
    django-admin startproject <name> .
    ```

5. **Create APP:**

    **Windows:**
    ```
    python -m django startapp <name>
    ```
    **MacOS:**
    ```
    python3 -m django startapp <name>
    ```

    **OR**

    **Windows:**
    ```
    python manage.py startapp <name>
    ```
    **MacOS:**
    ```
    python3 manage.py startapp <name>
    ```

6. **Run Server:**

    ```
    cd myproject
    ```

    **Windows:**
    ```
    python manage.py runserver
    ```
    **MacOS:**
    ```
    python3 manage.py runserver
    ```

7. **Deactive Environment:**

    ```
    deactivate
    ```

## Overview

By working through the lessons in this course, you've learned the necessary skills and knowledge to create a website in Django by creating a project and an app.

You were provided with code snippets and tasked with using these, plus your own code, to create a website that showcases the menu pages of the Little Lemon restaurant.

Users visit the homepage and can navigate to the pages About, Menu and Book using the main menu.

The menu page contains a list of the menu items that are stored in the database. Each menu item has been added using the Django Administration user interface and contains the following information:

- Name
- Price
- Description
- Image

Each menu item contains a link that displays a dedicated page for the individual item.

You will now take part in a peer review exercise in which you will submit your completed project for two of your peers to review. You will also be required to review a project of two of your peers.

The grading criteria are covered in more detail below.

****Review criterialess**

When you submit your assignment, other learners in the course will review and grade your work. They will evaluate the following:

- Does the homepage have a menu link that loads the menu page?
- Does the menu page contain a list of the menu items?
- Are the menu items displayed in alphabetical order?
- Do the menu items display with their associated price?
- Can you click on the menu items to navigate to the menu item page?
- Does the menu item page display all the information for that particular menu item?
- Does the website contain a footer section

****Example Submissionsless**

Here are some examples to help you understand what your assignment should look like.

**http://127.0.0.1:8000/menu/**

![dTpn_YnHSrGRTqAIFhr3fQ_4515bd5fa705424e93df69023f33fce1_peer-review-menu-page.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/2be64925-bc8b-4b89-9025-3b4d9abb6eec/dTpn_YnHSrGRTqAIFhr3fQ_4515bd5fa705424e93df69023f33fce1_peer-review-menu-page.png)

**http://127.0.0.1:8000/menu_item/1/**

![ix6y6CCNRTaszL_eBNW7eA_8b1855e7e98a46ec9b8f5f4a9e04f2e1_peer-review-menu-item-page.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/4579cd26-8aa6-4825-91b6-719a5b29849f/ix6y6CCNRTaszL_eBNW7eA_8b1855e7e98a46ec9b8f5f4a9e04f2e1_peer-review-menu-item-page.png)

**Note:** The id is automatically assigned to each menu item in incremental order as you add them using Django admin.

****How to create and submit your projectless**

Your project will be built using the VS Code editor inside the Coursera lab.  When you are happy that the code is working and you have tested the project in the browser, you must perform the following steps to export the project to your local machine.

## Export Django project

**Step 1:**

Select the lab files link at the top of the lab.

![XX--gEj5QPO8EsOGi2IoLA_30d83b9ab7134f34b804c664aa4ba1e1_lab-files-unchecked.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/18bfe32f-b728-4c56-8b0f-60e0372a855b/XX--gEj5QPO8EsOGi2IoLA_30d83b9ab7134f34b804c664aa4ba1e1_lab-files-unchecked.png)

**Step 2:**

Using the checkbox, select all the lab files.

**Tip:** To select all the labs at once, click the checkbox beside the word **Name**

![ypd1b2hESAaoLfw4hM8nQQ_acd6b2c3cb444dd4a6d3f52b081b38e1_select-lab-files.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/f9be24f4-d4df-46fd-9a33-398a2bc37e2d/ypd1b2hESAaoLfw4hM8nQQ_acd6b2c3cb444dd4a6d3f52b081b38e1_select-lab-files.png)

**Step 3:**

Click the download link to download all the files. Note that the files will download in .zip format

![9i-hSof5RDOn1Us4bbN4oQ_4918a8b3879a444a874fa599ca40e1e1_download-lab-files.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/44eb7f38-60a3-43f2-9ec1-8abef891f7e5/9i-hSof5RDOn1Us4bbN4oQ_4918a8b3879a444a874fa599ca40e1e1_download-lab-files.png)

**Step 4:**

Once the .zip file has downloaded to your local machine, you must extract it.

To learn more about how to zip and unzip folders visit the [Mac](https://support.apple.com/en-ie/guide/mac-help/mchlp2528/mac) or [Windows](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc) support page.

Once the zip file is extracted locate the folder **littlelemon** at the following path:

**Files > Files > home > coder > project**

![RdKyCmX1QvCCa3W9sz9MUQ_17f27c3876f3405b9a2bcce409aa74e1_project-path.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/6a252840-5042-4d3e-aa01-3c49947d7992/RdKyCmX1QvCCa3W9sz9MUQ_17f27c3876f3405b9a2bcce409aa74e1_project-path.png)

The folder named **littlelemon** is your project folder. Now you must zip this folder so you can upload it to the Coursera platform.

**Step 5:**

Zip the **littlelemon** project folder. To learn more about how to zip and unzip folders visit the [Mac](https://support.apple.com/en-ie/guide/mac-help/mchlp2528/mac) or [Windows](https://support.microsoft.com/en-us/windows/zip-and-unzip-files-f6dde0a7-0fec-8294-e1d3-703ed85e7ebc) support page.

![I0BPSqbDRL6IS4LC2zIe8w_7dc4a1094de6479fa31c7658472a62e1_little-lemon-project-zipped.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/d57ac92c-ab0d-4436-a026-c938d8ad6aba/I0BPSqbDRL6IS4LC2zIe8w_7dc4a1094de6479fa31c7658472a62e1_little-lemon-project-zipped.png)

Once you create the **littlelemon** folder in .zip format, you are ready to upload the project for peer review.

## Upload Django project for peer review

Upload the folder **littlelemon.zip**. Your reviewers will download it and upload it to the sandbox lab and follow the instructions provided to test the code. The output of their interactions with your app will show whether the required functionality has been implemented.

**Step 1:**

Open the lesson [Peer-graded Assignment: Peer review rubric: Design and Build a simple Django app](https://www.coursera.org/learn/django-web-framework/peer/68wd1/peer-review-rubric-design-and-build-a-simple-django-app)

**Step 2:**

Click on the **My Submission** tab and fill in the field for the **Project Title**. You can use your unique coder code assigned to you in the lab, for example **coder@83f6c42e40ee**.

Next, click the **Upload File** button.

![8LcrFssSQUyN_Vn84fU2hQ_ca21d5c2ca264e08908090c98a55b2e1_my-submission.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/123dd3f3-555a-45b5-8114-beb39dd0718b/8LcrFssSQUyN_Vn84fU2hQ_ca21d5c2ca264e08908090c98a55b2e1_my-submission.png)

Locate the **littlelemon.zip** file and upload it. Click the **Coursera Honor Code** checkbox and then click the **Preview** button. To finish, click the **Submit** button.

![0LSZCHjYRbiZMfned8fXdg_2cfe917b903041cd9af37a364d8840e1_project-preview.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/ff774152-207c-451a-8be4-a84fcc96ea6e/0LSZCHjYRbiZMfned8fXdg_2cfe917b903041cd9af37a364d8840e1_project-preview.png)

****How to review a projectless**

Once you have submitted your Django project, you are required to review two of your peers' submissions. You can view the peers that you need to review in the "Peers to review" section.

The steps are as follows.

## Download the Django project of your peer

**Step 1:**
Click the **Review assignments** button

![a6rCXT-fRCy6zUhEG3iO_A_0253ca4d280047c7b4bdf33fc62f28e1_review-assignments.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/1cd7a01e-15e4-4faf-91ff-fd7f3e3ae4ca/a6rCXT-fRCy6zUhEG3iO_A_0253ca4d280047c7b4bdf33fc62f28e1_review-assignments.png)

**Step 2:** 
Read the instructions under the heading **Review fellow learners** and press the **Start Reviewing** button.

![myyXF8MvQoCKJuNSzYlPgw_153020c6ece44ebebb0729c9bc0117e1_start-reviewing.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/de1096b7-5a86-4a0e-a92d-7b16aa94653a/e61b1b45-adf3-4c3a-a7f4-e3b124100d9f/myyXF8MvQoCKJuNSzYlPgw_153020c6ece44ebebb0729c9bc0117e1_start-reviewing.png)

Download the project of your peer to your local machine using the link provided.

**Note:** The project folder will be in **.zip** format.

## Upload the Django project of your peer to the sandbox lab

**Step 1:**

[Open the Peer review sandbox](https://www.coursera.org/learn/django-web-framework/ungradedLab/sr8rM/peer-review-sandbox) and follow the instructions.

**Step 2:**

Upload the Django project using the instructions in the Peer review sandbox.

**Step 3:**

Run the development server and open the project in the browser at URL **http://127.0.0.1:8000/**

**Step 4:**

Open a new tab in your web browser and open the peer review page. Review the website and answer the questions.

****Examples of Good Feedbackless**

As a reviewer, you will be required to provide feedback on assignments submitted by two of your peers.

The focus of your feedback should be on the functionality of the app.

Follow the prompts and look for the expected output. If you notice any errors in the functionality of any of the elements of the website, you will have the opportunity to provide guidance to your peers on how they might fix the error.

An example of good feedback would be:

*The project contained all of the actions expected. However on the menu page, the menu item did not display as a hyperlink. I would suggest reviewing the code to create the hyperlink*.