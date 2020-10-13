import { Component, Input, OnInit } from '@angular/core';
import { User } from '../shared/user.model';
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

  constructor(private service:CrudService, private router: Router) { }
  
  @Input() user:any;
  Username:string;
  FullName:string;
  Email:string;
  Password:string;
  UserAge:number;


  resetForm(form?:NgForm) {
    if (form != null) {
      form.reset();
    }
    this.user = {
      UserID: "",
      Username: "",
      FullName: "",
      Email: "",
      Password: "",
      UserAge: 0,
    }
  }
  
  ngOnInit(): void {
    this.Username=this.user.Username;
    this.FullName=this.user.FullName;
    this.Email=this.user.Email;
    this.Password=this.user.Password;
    this.UserAge=this.user.UserAge;
  }

  public CalculateAge(): void {
    if (this.birthdate) {
      var timeDiff = Math.abs(Date.now() - this.birthdate.getTime());
      this.UserAge = Math.floor(timeDiff / (1000 * 3600 * 24) / 365.25);
    }
  }

  signup() {
    var val = {
                Username:this.Username,
                FullName:this.FullName,
                Email:this.Email,
                Password:this.Password,
                UserAge:this.UserAge,
                }
    this.service.addUser(val).subscribe(result => {
      this.router.navigate(["/login"])
    });

  }
  

}
