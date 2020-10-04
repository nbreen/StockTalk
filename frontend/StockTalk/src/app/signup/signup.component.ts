import { Component, OnInit } from '@angular/core';
import { User } from '../shared/user.model'
import { NgForm} from '@angular/forms'

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  user:User;
  create_account() {
    
  }
  constructor() { }

  resetForm(form?:NgForm) {
    if (form != null) {
      form.reset();
    }
    this.user = {
      username: "",
      full_name: "",
      email: "",
      password1: "",
      password2: "",
    }
  }

  ngOnInit(): void {
    this.resetForm();
  }

}
