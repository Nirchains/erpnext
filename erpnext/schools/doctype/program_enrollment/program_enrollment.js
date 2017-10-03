// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

cur_frm.add_fetch('fee_structure', 'total_amount', 'amount');

frappe.ui.form.on("Program Enrollment", {
	onload: function(frm, cdt, cdn){
		frm.set_query("academic_term", "fees", function(){
			return{
				"filters":{
					"academic_year": (frm.doc.academic_year)
				}
			};
		});

		frm.fields_dict['fees'].grid.get_field('fee_structure').get_query = function(doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				filters: {'academic_term': d.academic_term}
			}
		};

		if (frm.doc.program) {
			frm.set_query("course", "courses", function(doc, cdt, cdn) {
				return{
					query: "erpnext.schools.doctype.program_enrollment.program_enrollment.get_program_courses",
					filters: {
						'program': frm.doc.program
					}
				}
			});
		}

		frm.set_query("student", function() {
			return{
				query: "erpnext.schools.doctype.program_enrollment.program_enrollment.get_students",
				filters: {
					'academic_year': frm.doc.academic_year,
					'academic_term': frm.doc.academic_term
				}
			}
		});
	},

	program: function(frm) {
		frm.events.get_courses(frm);
		if (frm.doc.program) {
			frappe.call({
				method: "erpnext.schools.api.get_fee_schedule",
				args: {
					"program": frm.doc.program,
					"student_category": frm.doc.student_category
				},
				callback: function(r) {
					if(r.message) {
						frm.set_value("fees" ,r.message);
						frm.events.get_courses(frm);
					}
				}
			});
		}
	},

	student_category: function() {
		frappe.ui.form.trigger("Program Enrollment", "program");
	},

	get_courses: function(frm) {
		frm.set_value("courses",[]);
		frappe.call({
			method: "get_courses",
			doc:frm.doc,
			callback: function(r) {
				if(r.message) {
					frm.set_value("courses", r.message);
				}
			}
		})
	}
});
