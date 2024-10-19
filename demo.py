import streamlit as st
from pdf_data import pdfs  # Import the PDF data
import streamlit as st
import os
import json
from github import Github
import base64
import ast

# Set Page Configuration
st.set_page_config(page_title="PDF Library", layout="wide")

# Define a function to render the user page
def render_user_page():
    # Main Page Filters
    st.header("MEST Course outlines (McMaster University)")

    # Layout for filters in a single row
    col1, col2, col3, col4, col5 = st.columns([3, 3, 3, 4, 1])

    with col1:
        # First Filter: Stream
        stream_options = [
            "Automotive Stream",
            "Automation and Smart Systems",
            "Digital Manufacturing",
            "Process Systems Stream",
            "All stream course"
        ]
        selected_streams = st.multiselect("Select Stream(s)", stream_options)

    with col2:
        # Second Filter: Course Type
        course_type_options = [
            "Required core courses",
            "Professional Development course",
            "Core course",
            "Recommended Technical electives",
            "Cross-Disciplinary Elective Course",
            "Other elective course"
        ]
        selected_course_types = st.multiselect("Select Course Type(s)", course_type_options)

    with col3:
        # Third Filter: Semester
        semester_options = ["Fall", "Winter", "Summer"]
        selected_semesters = st.multiselect("Select Semester(s)", semester_options)

    # Search Bar and Button in a single row with placeholder
    with col4:
        search_query = st.text_input("", placeholder="Search for a course")

    with col5:
        st.write("")  # Add some spacing
        search_button = st.button("Search")

    st.markdown("---")

    # Function to filter PDFs based on selections and search
    def filter_pdfs(pdfs, streams, course_types, semesters, search):
        filtered = pdfs

        # Filter by Stream
        if streams:
            # Map stream options to subcategories
            stream_map = {
                "Automotive Stream": "Automotive Stream",
                "Automation and Smart Systems": "Automation and Smart Systems",
                "Digital Manufacturing": "Digital Manufacturing",
                "Process Systems Stream": "Process Systems Stream",
                "All stream course": "All stream course"
            }
            selected_subcategories = [stream_map[stream] for stream in streams if stream in stream_map]
            filtered = [pdf for pdf in filtered if pdf["subcategory"] in selected_subcategories]

        # Filter by Course Type
        if course_types:
            filtered = [pdf for pdf in filtered if pdf["category"] in course_types]

        # Filter by Semester
        if semesters:
            filtered = [pdf for pdf in filtered if any(semester in pdf["semesters"] for semester in semesters)]

        # Filter by Search Query (only when search button is pressed)
        if search and search_button:
            search_lower = search.lower()
            filtered = [
                pdf for pdf in filtered
                if search_lower in pdf["name"].lower() or search_lower in pdf["label"].lower()
            ]

        return filtered

    # Apply Filters
    filtered_pdfs = filter_pdfs(pdfs, selected_streams, selected_course_types, selected_semesters, search_query)

    # Display PDFs as Cards
    st.subheader("MEST Course Outline PDFs")

    if not filtered_pdfs:
        st.info("No PDFs match the selected filters.")
    else:
        # Define the number of columns per row
        cols_per_row = 3
        for i in range(0, len(filtered_pdfs), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, pdf in enumerate(filtered_pdfs[i:i + cols_per_row]):
                with cols[j]:
                    # Render the card with HTML and CSS for styling
                    st.markdown(f"""
                        <div style="padding: 15px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                            <h3 style="color: #007bff; font-size: 20px;">{pdf['icon']} {pdf['name']}</h3>
                            <p style="font-weight: bold; font-size: 16px;">{pdf['label']}</p>
                            <p><strong>Category:</strong> {pdf['category']}</p>
                            <p><strong>Subcategory:</strong> {pdf['subcategory']}</p>
                            <p><strong>Semesters:</strong> {', '.join(pdf['semesters'])}</p>
                            """, unsafe_allow_html=True)

                    try:
                        with open(pdf['file_path'], "rb") as f:
                            pdf_data = f.read()
                        st.download_button(
                            label="Download PDF",
                            data=pdf_data,
                            file_name=f"{pdf['name']}.pdf",
                            mime="application/pdf"
                        )
                    except FileNotFoundError:
                        st.error("File not found.")
                    st.markdown("</div>", unsafe_allow_html=True)

# Define a function to render the admin page
def render_admin_page():
    # Set Page Configuration
    # st.set_page_config(page_title="Admin Course Management", layout="wide")

    # Define categories, subcategories, and semesters for selection
    course_type_options = [
        "Required core courses",
        "Professional Development course",
        "Core course",
        "Recommended Technical electives",
        "Cross-Disciplinary Elective Course",
        "Other elective course"
    ]

    stream_options = [
        "Automotive Stream",
        "Automation and Smart Systems",
        "Digital Manufacturing",
        "Process Systems Stream",
        "All stream course"
    ]

    semester_options = ["Fall", "Winter", "Summer"]

    # GitHub repository details
    github_token = st.secrets["GITHUB_TOKEN"]  # Store token securely using Streamlit secrets
    # github_token = st.secrets.get("GITHUB_TOKEN")
    repo_name = "meetpatel1812/mcmaster_course_outline_app"
    file_path = "pdf_data.py"  # Update this with the correct path in your repo

    # Initialize GitHub instance
    g = Github(github_token)
    repo = g.get_repo(repo_name)

    # Function to fetch courses from GitHub
    # def fetch_courses():
    #     contents = repo.get_contents(file_path)
    #     file_content = contents.decoded_content.decode("utf-8")
    #     exec(file_content)  # This will load the `pdfs` variable
    #     return pdfs

    import ast

    # Function to fetch courses from GitHub
    def fetch_courses():
        contents = repo.get_contents(file_path)
        file_content = contents.decoded_content.decode("utf-8")
        
        # Safely parse the content to extract 'pdfs' list
        parsed_content = ast.parse(file_content)
        
        # Look for the 'pdfs' variable in the parsed content
        for node in parsed_content.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == 'pdfs':
                        return ast.literal_eval(node.value)
        return []

    # Fetch existing courses from GitHub
    try:
        courses = fetch_courses()
        if not courses:
            st.warning("No courses found in the repository.")
    except Exception as e:
        st.error(f"Error loading courses from GitHub: {str(e)}")
        courses = []

    # Course Addition, Modification, and Deletion Header
    st.header("Admin Course Management")

    # # Fetch existing courses from GitHub
    # try:
    #     courses = fetch_courses()
    # except Exception as e:
    #     st.error(f"Error loading courses from GitHub: {str(e)}")
    #     courses = []

    # Course Addition Form
    st.subheader("Add / Modify Course")
    st.divider()
    # Select course for modification
    course_names = [course['name'] for course in courses]
    selected_course_name = st.selectbox("Select a Course to Modify (or leave blank to add a new course)", [""] + course_names)
    st.divider()
    # If a course is selected, load its details for modification
    if selected_course_name:
        selected_course = next((course for course in courses if course["name"] == selected_course_name), None)
        if selected_course:
            st.info(f"Modifying: {selected_course_name}")
            course_name = st.text_input("Course Name", selected_course['name'])
            course_label = st.text_input("Course Label", selected_course['label'])
            category = st.selectbox("Select Course Type", course_type_options, index=course_type_options.index(selected_course['category']))
            subcategory = st.selectbox("Select Stream", stream_options, index=stream_options.index(selected_course['subcategory']))
            semesters = st.multiselect("Select Semester(s)", semester_options, default=selected_course['semesters'])
            uploaded_file = st.file_uploader("Upload Course Outline PDF (leave blank to keep current)", type=["pdf"])
        else:
            st.error("Selected course not found.")
    else:
        # Default empty form for new course
        course_name = st.text_input("Course Name")
        course_label = st.text_input("Course Label")
        category = st.selectbox("Select Course Type", course_type_options)
        subcategory = st.selectbox("Select Stream", stream_options)
        semesters = st.multiselect("Select Semester(s)", semester_options)
        uploaded_file = st.file_uploader("Upload Course Outline PDF", type=["pdf"])

    # Submit button
    submitted = st.button("Submit Course")

    if submitted:
        # Ensure all fields are filled
        if not course_name or not course_label or not semesters:
            st.error("Please fill all fields.")
        else:
            # Prepare course data
            course_data = {
                "name": course_name,
                "label": course_label,
                "category": category,
                "subcategory": subcategory,
                "semesters": semesters,
                "file_path": f"Course/{category.replace(' ', '_')}/{uploaded_file.name if uploaded_file else selected_course['file_path'].split('/')[-1]}",
                "icon": ""
            }

            # Handle course addition or modification
            if selected_course_name:
                # Modify existing course
                st.info("Updating course information...")
                courses = [course_data if course['name'] == selected_course_name else course for course in courses]
            else:
                # Add new course
                courses.append(course_data)

            # Save the PDF file to GitHub (if a new file is uploaded)
            if uploaded_file:
                try:
                    pdf_content = uploaded_file.getvalue()
                    pdf_github_path = f"Course/{category.replace(' ', '_')}/{uploaded_file.name}"

                    try:
                        existing_file = repo.get_contents(pdf_github_path)
                        repo.update_file(
                            path=pdf_github_path,
                            message=f"Update PDF for {course_name}",
                            content=pdf_content,
                            sha=existing_file.sha
                        )
                    except:
                        repo.create_file(
                            path=pdf_github_path,
                            message=f"Add PDF for {course_name}",
                            content=pdf_content
                        )
                    st.success("PDF uploaded successfully!")
                except Exception as e:
                    st.error(f"Error uploading PDF: {str(e)}")

            # Update the `pdf_data.py` file
            try:
                pdfs_list = json.dumps(courses, indent=4)
                pdfs_code = f"pdfs = {pdfs_list}"
                repo.update_file(
                    path=file_path,
                    message="Update course data",
                    content=pdfs_code,
                    sha=repo.get_contents(file_path).sha
                )
                st.success("Course data updated successfully!")
            except Exception as e:
                st.error(f"Error updating course data on GitHub: {str(e)}")
    st.divider()
    # # Course Deletion Section
    # st.subheader("Delete Course")

    # # Select course for deletion
    # course_to_delete = st.selectbox("Select a Course to Delete", course_names)

    # # Delete button
    # if st.button("Delete Course"):
    #     if course_to_delete:
    #         # Filter out the selected course
    #         courses = [course for course in courses if course["name"] != course_to_delete]

    #         # Remove associated PDF from GitHub
    #         try:
    #             course_to_delete_data = next(course for course in courses if course["name"] == course_to_delete)
    #             pdf_github_path = course_to_delete_data['file_path']

    #             # Delete the PDF file from GitHub
    #             try:
    #                 existing_file = repo.get_contents(pdf_github_path)
    #                 repo.delete_file(
    #                     path=pdf_github_path,
    #                     message=f"Delete PDF for {course_to_delete}",
    #                     sha=existing_file.sha
    #                 )
    #                 st.success("PDF deleted successfully!")
    #             except:
    #                 st.warning("PDF file not found in the repository.")
    #         except StopIteration:
    #             st.error("Course not found.")

    #         # Update the `pdf_data.py` file
    #         try:
    #             pdfs_list = json.dumps(courses, indent=4)
    #             pdfs_code = f"pdfs = {pdfs_list}"
    #             repo.update_file(
    #                 path=file_path,
    #                 message="Delete course data",
    #                 content=pdfs_code,
    #                 sha=repo.get_contents(file_path).sha
    #             )
    #             st.success("Course deleted successfully!")
    #         except Exception as e:
    #             st.error(f"Error updating course data on GitHub: {str(e)}")
    #     else:
    #         st.error("Please select a course to delete.")

    st.subheader("Delete Course")

    # Select course for deletion
    course_to_delete = st.selectbox("Select a Course to Delete", course_names)

    # Delete button
    if st.button("Delete Course"):
        if course_to_delete:
            try:
                # Find the course details before filtering it out
                course_to_delete_data = next(course for course in courses if course["name"] == course_to_delete)
                pdf_github_path = course_to_delete_data['file_path']  # Store the file path for later use

                # Remove the course from the courses list
                courses = [course for course in courses if course["name"] != course_to_delete]

                # Remove associated PDF from GitHub
                try:
                    existing_file = repo.get_contents(pdf_github_path)
                    repo.delete_file(
                        path=pdf_github_path,
                        message=f"Delete PDF for {course_to_delete}",
                        sha=existing_file.sha
                    )
                    st.success("PDF deleted successfully!")
                except:
                    st.warning("PDF file not found in the repository.")

                # Update the `pdf_data.py` file with the new courses list
                try:
                    pdfs_list = json.dumps(courses, indent=4)
                    pdfs_code = f"pdfs = {pdfs_list}"
                    repo.update_file(
                        path=file_path,
                        message="Delete course data",
                        content=pdfs_code,
                        sha=repo.get_contents(file_path).sha
                    )
                    st.success("Course deleted successfully!")
                except Exception as e:
                    st.error(f"Error updating course data on GitHub: {str(e)}")

            except StopIteration:
                st.error("Course not found.")
        else:
            st.error("Please select a course to delete.")
    st.divider()
    st.subheader("List of Courses that already added")
    st.divider()

    try:
        # Fetch the file from the repository
        contents = repo.get_contents(file_path)
        file_content = contents.decoded_content.decode("utf-8")

        # Parse the 'pdfs' list from the file content
        exec(file_content)  # Execute the file content to load the `pdfs` list

        for course in pdfs:
            st.write(f"**{course['name']}** - {course['label']} ({course['category']})")
    except Exception as e:
        st.error(f"Error loading courses from GitHub: {str(e)}")

        # Add your admin page code here

    # Handle page switching using session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'user'

# Show the user page or admin page based on session state
if st.session_state.current_page == 'user':
    render_user_page()
    # Add a button to switch to the admin page
    if st.button("Switch to Admin Page"):
        st.session_state.current_page = 'admin'
elif st.session_state.current_page == 'admin':
    render_admin_page()
    # Add a button to switch back to the user page
    if st.button("Switch to User Page"):
        st.session_state.current_page = 'user'
