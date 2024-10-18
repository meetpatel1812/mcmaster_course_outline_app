# pdf_data.py
        # "Required core courses",
        # "Professional Development course",
        # "Core course",
        # "Recommended Technical electives",
        # "Cross-Disciplinary Elective Course",
        # "Other elective course"

        # "Automotive Stream",
        # "Automation and Smart Systems",
        # "Digital Manufacturing",
        # "Process Systems Stream",
        # "All stream course"


pdfs = [
    {
        "name": "SEP 769",
        "label": "Cyber Physical Systems",
        "category": "Required core courses",
        "subcategory": "All stream course",
        "semesters": ["Fall", "Winter","Summer"],
        "file_path": "Course/Required_courses/SEP769 - Fall2023.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 6TC3",
        "label": "Technical Communications",
        "category": "Professional Development",
        "subcategory": "All stream course",
        "semesters": ["Fall","Winter"],
        "file_path": "Course/Professional_Developement_courses/SEP 6TC3 Course Outline Fall 2023 - Copy Dulcie.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 725",
        "label": "Practical Project Management for Today's Business Environment",
        "category": "Professional Development",
        "subcategory": "All stream course",
        "semesters": ["Fall", "Summer","Winter"],
        "file_path": "Course/Professional_Developement_courses/SEP 725 Fall 2023 Course Outline.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 773",
        "label": "Leadership for Innovation",
        "category": "Professional Development",
        "subcategory": "All stream course",
        "semesters": ["Fall", "Summer","Winter"],
        "file_path": "Course/Professional_Developement_courses/SEP 773 Fall 2023 Course Outline Official Mac .pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 760",
        "label": "Design Thinking",
        "category": "Professional Development",
        "subcategory": "All stream course",
        "semesters": ["Fall","Winter"],
        "file_path": "Course/Professional_Developement_courses/SEP 760 Fall 2023 — Course Outline.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 6AE3",
        "label": "Internal Combustion Engines",
        "category": "Core course",
        "subcategory": "Automotive Stream",
        "semesters": ["Winter"],
        "file_path": "Course/Automotive_stream/Core_Courses/SEP 6AE3_Outline_24a.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 6DV3",
        "label": "Vehicle Dynamics",
        "category": "Core course",
        "subcategory": "Automotive Stream",
        "semesters": ["Fall"],
        "file_path": "Course/Automotive_stream/Core_Courses/SEP 6DV3 Fall 2023 Course Outline.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 711",
        "label": "Electric Powertrain Components Design",
        "category": "Core course",
        "subcategory": "Automotive Stream",
        "semesters": ["Fall"],
        "file_path": "Course/Automotive_stream/Core_Courses/SEP711_Outline_23c.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 722",
        "label": "Electric Drive Vehicles (MECH ENG 760)",
        "category": "Core course",
        "subcategory": "Automotive Stream",
        "semesters": ["Fall"],
        "file_path": "Course/Automotive_stream/Core_Courses/SEP 722 MECH760_Outline_23c.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 740",
        "label": "Deep Learning",
        "category": "Core course",
        "subcategory": "Automotive Stream",
        "semesters": ["Fall","Winter","Summer"],
        "file_path": "Course/Automotive_stream/Core_Courses/SEP 740 Deep Learning - Summer 2024 - Course Outline.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 742",
        "label": "Visual Perception for Autonomus Vehicles",
        "category": "Core course",
        "subcategory": "Automotive Stream",
        "semesters": ["Winter"],
        "file_path": "Course/Automotive_stream/Core_Courses/SEP 742 Visual Perception - Winter 2024 - Course Outline.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 775",
        "label": "Introduction to Computational Natural Language Processing",
        "category": "Core course",
        "subcategory": "Automotive Stream",
        "semesters": ["Winter"],
        "file_path": "Course/Automotive_stream/Core_Courses/SEP 775 NLP - Winter 2024 - Course Outline.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 780",
        "label": "Advance Robotics and Automation",
        "category": "Recommended Technical electives",
        "subcategory": "Automotive Stream",
        "semesters": ["Winter","Fall"],
        "file_path": "Course/Automotive_stream/Recommended_technical_electives/SEP 780 Fall 2023 Course Outline rev 1.pdf",
        "icon": "📄"
    },
     {
        "name": "SEP 783",
        "label": "Sensors and Actuators",
        "category": "Recommended Technical electives",
        "subcategory": "Automotive Stream",
        "semesters": ["Winter"],
        "file_path": "Course/Automotive_stream/Recommended_technical_electives/SEP 783-W2024 Course Outline-Formal.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 791",
        "label": "Augmented Reality, Virtual Reality and Mixed Reality",
        "category": "Recommended Technical electives",
        "subcategory": "Automotive Stream",
        "semesters": ["Winter"],
        "file_path": "Course/Automotive_stream/Recommended_technical_electives/SEP 791 (C01) Course Outline.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 709",
        "label": "Engineering Issues, Technology and Public Policy",
        "category": "Cross-Disciplinary Elective Course",
        "subcategory": "Automotive Stream",
        "semesters": ["Fall"],
        "file_path": "Course/Automotive_stream/Cross_Disciplinary/SEP 709outline23.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 710",
        "label": "International Governance and Environmental Sustainability",
        "category": "Cross-Disciplinary Elective Course",
        "subcategory": "Automotive Stream",
        "semesters": ["Winter"],
        "file_path": "Course/Automotive_stream/Cross_Disciplinary/SEP 710 Winter 2024outline revised.pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 770",
        "label": "Total Sustainability Management",
        "category": "Cross-Disciplinary Elective Course",
        "subcategory": "Automotive Stream",
        "semesters": ["Winter","Fall","Summer"],
        "file_path": "Course/Automotive_stream/Cross_Disciplinary/SEP 770 Course Outline (1).pdf",
        "icon": "📄"
    },
    {
        "name": "SEP 705",
        "label": "Green Engineering, Sustainability and Public Policy",
        "category": "Cross-Disciplinary Elective Course",
        "subcategory": "Automotive Stream",
        "semesters": ["Fall"],
        "file_path": "Course/Automotive_stream/Cross_Disciplinary/SEP 705 GREEN ENGINEERINGoutline fall 2023.pdf",
        "icon": "📄"
    },
    
    


    # Add more PDFs as needed

   
    {
    "name": "meet",
    "label": "meet",
    "category": "Required core courses",
    "subcategory": "Automotive Stream",
    "semesters": [
        "Fall"
    ],
    "file_path": "Course/Required core courses/Meet_Transcript.pdf",
    "icon": ""
},]
