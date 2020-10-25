import { stringify } from 'querystring';
import { CrudService } from 'src/app/crud.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../Interfaces';
import { Globals } from '../Globals';

@Component({
  selector: 'app-delete-user',
  templateUrl: './delete-user.component.html',
  styleUrls: ['./delete-user.component.scss'],
  providers: [CrudService]
})
export class DeleteUserComponent implements OnInit {

  understand = false;
  currentUsername: String;

  constructor(private router: Router, private backend: CrudService, private globals: Globals) {
    this.currentUsername = this.globals.currentUsername;
  }
  
  deleteAccount() {
    console.log(this.understand);
    if (this.understand == false) {
      console.log("Checkbox!");
      alert("Please verify that you want to delete your account!");
    } else {
      // Delete Account
      this.backend.deleteAccount(46).subscribe(result => {
        alert(result);
        this.router.navigate(['/login']);
      });
    }
  }

  ngOnInit(): void {
  }

}
