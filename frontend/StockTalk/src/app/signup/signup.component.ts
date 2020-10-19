import { Component, Input, OnInit } from '@angular/core';
import { User } from '../Interfaces';
import { NgForm} from '@angular/forms';
import { CrudService } from 'src/app/crud.service';
import { Router, RouterModule } from '@angular/router';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  public birthdate: Date;

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

  public CalculateAge(): void {
    if (this.birthdate) {
      var timeDiff = Math.abs(Date.now() - this.birthdate.getTime());
      this.user.UserAge = Math.floor(timeDiff / (1000 * 3600 * 24) / 365.25);
    }
  }

  signup() {
    this.service.addUser(this.user).subscribe(result => {
      this.router.navigate(["/login"])
    });

  }
  

}
