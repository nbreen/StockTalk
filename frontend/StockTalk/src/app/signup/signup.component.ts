import { Component, Input, OnInit } from '@angular/core';
import { User } from '../Interfaces';
import { NgForm} from '@angular/forms';
import { CrudService } from 'src/app/crud.service';
import { Router, RouterModule } from '@angular/router';
import { nullSafeIsEquivalent } from '@angular/compiler/src/output/output_ast';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  public Password2: "";

  constructor(private service: CrudService, private router: Router) { }
  
  @Input() user: User = {
    Username: "",
    FullName: "",
    Email: "",
    Password: "",
    UserAge: 0
  };
  
  resetForm(form?:NgForm) {
    if (form != null) {
      form.reset();
    }

    this.user.Username = "";
    this.user.FullName = "";
    this.user.Email = "";
    this.user.Password = "";
    this.user.UserAge = 0;
  }
  
  ngOnInit(): void { }


  signup() {

    if (this.user.Password != this.Password2) {
      let error: string = "Passwords are not the same"
      alert(error);
      return;
    }



    this.service.addUser(this.user).subscribe(res => {
      alert(res.toString());
      if (res.toString().match("User added successfully") === null) {
      } else {
        this.router.navigate(["/login"])
      }
    });

  }
  

}
