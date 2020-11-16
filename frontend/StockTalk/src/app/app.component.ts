import { CrudService } from './crud.service';
import { Router } from '@angular/router';
import { Globals } from './Globals';
import { Component } from '@angular/core';
import { Profile } from './shared/profile.model';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent {

  title = 'StockTalk';
  test_profile: Profile;

  constructor(private router: Router, private backend: CrudService, public globals: Globals) {
  }

  public reload() {
  }



  ngOnInit() {
    this.globals.currentUsername = localStorage.getItem("currentUsername");
    if (localStorage.getItem("isAuthenticated") == "false") {
      // Current user is authenticated
      this.globals.isAuthenticated = false;
    } else {
      // Current user is NOT authenticated
      this.globals.isAuthenticated = true;
    }

  }

  directProfile() {
    // this.router.navigate(["/profile/" + this.globals.currentUsername]);
    this.router.navigate(["/profile/" + this.globals.currentUsername]) .then(() => {
      window.location.reload();
    });
  }

  directSavedPosts() {
    this.router.navigate(["/mysavedposts/"]) .then(() => {
      window.location.reload();
    });
  }

  directSuggestions() {
    this.router.navigate(["/suggestions/"]) .then(() => {
      window.location.reload();
    });
  }
  

  public logout() {

    if (confirm("Are you sure you want to logout?")) {
      localStorage.setItem("isAuthenticated", "false");
      localStorage.setItem("currentUsername", "");
      localStorage.setItem("sortAZ", "false");
      localStorage.setItem("sortCount", "false");
      this.globals.isAuthenticated = false;
      this.router.navigate(["/"]);
    }

  }

}
