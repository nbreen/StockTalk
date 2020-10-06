import { Component, Input, OnInit } from '@angular/core';
import { User } from '../shared/user.model';
import { NgForm} from '@angular/forms';
import { CrudService } from 'src/app/crud.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent implements OnInit {

  public birthdate: Date;

  constructor(private service:CrudService) { }
  
  @Input() user:any;
  UserID:string;
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
      UserAge: 0
    }
  }
  
  ngOnInit(): void {
    this.UserID=this.user.UserID;
    this.Username=this.user.Username;
    this.FullName=this.user.FullName;
    this.Email=this.user.Email;
    this.Password=this.user.Password;
  }

  public CalculateAge(): void {
    if (this.birthdate) {
      var timeDiff = Math.abs(Date.now() - this.birthdate.getTime());
      this.UserAge = Math.floor(timeDiff / (1000 * 3600 * 24) / 365.25);
    }
  }

  addUser() {
    var val = {UserID:this.UserID,
                Username:this.Username,
                FullName:this.FullName,
                Email:this.Email,
                Password:this.Password,
                UserAge:this.UserAge}
    this.service.createUser(val).subscribe(res=>{
      alert(res.toString())});

  }
  

}
