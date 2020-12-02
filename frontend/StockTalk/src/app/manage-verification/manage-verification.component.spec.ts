import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ManageVerificationComponent } from './manage-verification.component';

describe('ManageVerificationComponent', () => {
  let component: ManageVerificationComponent;
  let fixture: ComponentFixture<ManageVerificationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ManageVerificationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ManageVerificationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
